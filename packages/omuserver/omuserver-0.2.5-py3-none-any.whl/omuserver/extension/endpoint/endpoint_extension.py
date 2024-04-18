from __future__ import annotations

import abc
from typing import Dict, List

from loguru import logger
from omu.extension.endpoint.endpoint_extension import (
    ENDPOINT_CALL_PACKET,
    ENDPOINT_ERROR_PACKET,
    ENDPOINT_RECEIVE_PACKET,
    ENDPOINT_REGISTER_PACKET,
    EndpointDataPacket,
    EndpointErrorPacket,
    EndpointType,
)
from omu.helper import Coro
from omu.identifier import Identifier

from omuserver.server import Server
from omuserver.session import Session


class Endpoint(abc.ABC):
    @property
    @abc.abstractmethod
    def identifier(self) -> Identifier: ...

    @abc.abstractmethod
    async def call(self, data: EndpointDataPacket, session: Session) -> None: ...


class SessionEndpoint(Endpoint):
    def __init__(self, session: Session, identifier: Identifier) -> None:
        self._session = session
        self._identifier = identifier

    @property
    def identifier(self) -> Identifier:
        return self._identifier

    async def call(self, data: EndpointDataPacket, session: Session) -> None:
        if self._session.closed:
            raise RuntimeError(f"Session {self._session.app.key()} already closed")
        await self._session.send(ENDPOINT_CALL_PACKET, data)


class ServerEndpoint[Req, Res](Endpoint):
    def __init__(
        self,
        server: Server,
        endpoint: EndpointType[Req, Res],
        callback: Coro[[Session, Req], Res],
    ) -> None:
        self._server = server
        self._endpoint = endpoint
        self._callback = callback

    @property
    def identifier(self) -> Identifier:
        return self._endpoint.identifier

    async def call(self, data: EndpointDataPacket, session: Session) -> None:
        if session.closed:
            raise RuntimeError("Session already closed")
        try:
            req = self._endpoint.request_serializer.deserialize(data["data"])
            res = await self._callback(session, req)
            json = self._endpoint.response_serializer.serialize(res)
            await session.send(
                ENDPOINT_RECEIVE_PACKET,
                EndpointDataPacket(type=data["type"], id=data["id"], data=json),
            )
        except Exception as e:
            await session.send(
                ENDPOINT_ERROR_PACKET,
                EndpointErrorPacket(type=data["type"], id=data["id"], error=str(e)),
            )
            raise e


class EndpointCall:
    def __init__(self, session: Session, data: EndpointDataPacket) -> None:
        self._session = session
        self._data = data

    async def receive(self, data: EndpointDataPacket) -> None:
        await self._session.send(ENDPOINT_RECEIVE_PACKET, data)

    async def error(self, error: str) -> None:
        await self._session.send(
            ENDPOINT_ERROR_PACKET,
            EndpointErrorPacket(
                type=self._data["type"], id=self._data["id"], error=error
            ),
        )


class EndpointExtension:
    def __init__(self, server: Server) -> None:
        self._server = server
        self._endpoints: Dict[Identifier, Endpoint] = {}
        self._calls: Dict[str, EndpointCall] = {}
        server.packet_dispatcher.register(
            ENDPOINT_REGISTER_PACKET,
            ENDPOINT_CALL_PACKET,
            ENDPOINT_RECEIVE_PACKET,
            ENDPOINT_ERROR_PACKET,
        )
        server.packet_dispatcher.add_packet_handler(
            ENDPOINT_REGISTER_PACKET, self._on_endpoint_register
        )
        server.packet_dispatcher.add_packet_handler(
            ENDPOINT_CALL_PACKET, self._on_endpoint_call
        )
        server.packet_dispatcher.add_packet_handler(
            ENDPOINT_RECEIVE_PACKET, self._on_endpoint_receive
        )
        server.packet_dispatcher.add_packet_handler(
            ENDPOINT_ERROR_PACKET, self._on_endpoint_error
        )

    async def _on_endpoint_register(
        self, session: Session, endpoint_identifiers: List[Identifier]
    ) -> None:
        for identifier in endpoint_identifiers:
            endpoint = SessionEndpoint(session, identifier)
            self._endpoints[identifier] = endpoint

    def bind_endpoint[Req, Res](
        self,
        type: EndpointType[Req, Res],
        callback: Coro[[Session, Req], Res],
    ) -> None:
        if type.identifier in self._endpoints:
            raise ValueError(f"Endpoint {type.identifier.key()} already bound")
        endpoint = ServerEndpoint(self._server, type, callback)
        self._endpoints[type.identifier] = endpoint

    async def _on_endpoint_call(
        self, session: Session, req: EndpointDataPacket
    ) -> None:
        endpoint = await self._get_endpoint(req, session)
        if endpoint is None:
            logger.warning(
                f"{session.app.key()} tried to call unknown endpoint {req['type']}"
            )
            await session.send(
                ENDPOINT_ERROR_PACKET,
                EndpointErrorPacket(
                    type=req["type"],
                    id=req["id"],
                    error=f"Endpoint {req['type']} not found",
                ),
            )
            return
        await endpoint.call(req, session)
        self._calls[f"{req['type']}:{req["id"]}"] = EndpointCall(session, req)

    async def _on_endpoint_receive(
        self, session: Session, req: EndpointDataPacket
    ) -> None:
        call = self._calls.get(f"{req['type']}:{req['id']}")
        if call is None:
            await session.send(
                ENDPOINT_ERROR_PACKET,
                EndpointErrorPacket(
                    type=req["type"],
                    id=req["id"],
                    error=f"Endpoint not found {req['type']}",
                ),
            )
            return
        await call.receive(req)

    async def _on_endpoint_error(
        self, session: Session, error: EndpointErrorPacket
    ) -> None:
        call = self._calls.get(f"{error['type']}:{error['id']}")
        if call is None:
            await session.send(
                ENDPOINT_ERROR_PACKET,
                EndpointErrorPacket(
                    type=error["type"],
                    id=error["id"],
                    error=f"Endpoint {error['type']} not found",
                ),
            )
        else:
            await call.error(error["error"])

    async def _get_endpoint(
        self, req: EndpointDataPacket, session: Session
    ) -> Endpoint | None:
        identifier = Identifier.from_key(req["type"])
        endpoint = self._endpoints.get(identifier)
        if endpoint is None:
            await session.send(
                ENDPOINT_ERROR_PACKET,
                EndpointErrorPacket(
                    type=req["type"],
                    id=req["id"],
                    error=f"Endpoint {req['type']} not found",
                ),
            )
            logger.warning(
                f"{session.app.key()} tried to call unconnected endpoint {req['type']}"
            )
            return
        return endpoint
