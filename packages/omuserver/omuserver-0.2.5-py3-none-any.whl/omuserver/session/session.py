from __future__ import annotations

import abc
import asyncio
from typing import TYPE_CHECKING, Tuple

from omu.event_emitter import EventEmitter
from omu.network.packet import PACKET_TYPES, Packet, PacketType
from omu.network.packet.packet_types import ConnectPacket

if TYPE_CHECKING:
    from omu import App
    from omu.network.packet_mapper import PacketMapper

    from omuserver.server import Server


class SessionConnection(abc.ABC):
    @abc.abstractmethod
    async def send(self, packet: Packet, packet_mapper: PacketMapper) -> None: ...

    @abc.abstractmethod
    async def receive(self, packet_mapper: PacketMapper) -> Packet | None: ...

    @abc.abstractmethod
    async def close(self) -> None: ...

    @property
    @abc.abstractmethod
    def closed(self) -> bool: ...


class Session:
    def __init__(
        self,
        packet_mapper: PacketMapper,
        app: App,
        token: str,
        is_dashboard: bool,
        connection: SessionConnection,
    ) -> None:
        self.serializer = packet_mapper
        self.app = app
        self.token = token
        self.is_dashboard = is_dashboard
        self._connection = connection
        self._listeners = SessionListeners()

    @classmethod
    async def from_connection(
        cls,
        server: Server,
        packet_mapper: PacketMapper,
        connection: SessionConnection,
    ) -> Session:
        packet = await connection.receive(packet_mapper)
        if packet is None:
            raise RuntimeError("Socket closed before connect")
        if packet.type != PACKET_TYPES.CONNECT:
            raise RuntimeError(
                f"Expected {PACKET_TYPES.CONNECT.identifier} but got {packet.type}"
            )
        if not isinstance(packet.data, ConnectPacket):
            raise RuntimeError(f"Invalid packet data: {packet.data}")
        event = packet.data
        token = event.token
        token, is_dashboard = await cls.verify_app_token(server, event, token)
        session = Session(packet_mapper, event.app, token, is_dashboard, connection)
        await session.send(PACKET_TYPES.TOKEN, token)
        return session

    @classmethod
    async def verify_app_token(
        cls, server: Server, connect_packet: ConnectPacket, token: str | None
    ) -> Tuple[str, bool]:
        if token is None:
            token = await server.security.generate_app_token(connect_packet.app)
        if token == server.config.dashboard_token:
            return token, True
        else:
            verified = await server.security.validate_app_token(
                connect_packet.app, token
            )
            if not verified:
                raise RuntimeError("Invalid token")
        return token, False

    @property
    def closed(self) -> bool:
        return self._connection.closed

    async def disconnect(self) -> None:
        await self._connection.close()
        await self._listeners.disconnected.emit(self)

    async def listen(self) -> None:
        try:
            while not self._connection.closed:
                packet = await self._connection.receive(self.serializer)
                if packet is None:
                    break
                asyncio.create_task(self._dispatch_packet(packet))
        finally:
            await self.disconnect()

    async def _dispatch_packet(self, packet: Packet) -> None:
        await self._listeners.packet.emit(self, packet)

    async def send[T](self, packet_type: PacketType[T], data: T) -> None:
        await self._connection.send(Packet(packet_type, data), self.serializer)

    @property
    def listeners(self) -> SessionListeners:
        return self._listeners


class SessionListeners:
    def __init__(self) -> None:
        self.packet = EventEmitter[Session, Packet]()
        self.disconnected = EventEmitter[Session]()
