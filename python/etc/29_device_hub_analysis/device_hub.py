from __future__ import annotations

import asyncio
import uuid
from socket import socket
from typing import Iterator, Self

from eventsystem import event, EventDispatcher

from utils.transport import ITransport
from protocol import zondcom_pb2
from protocol.message_type import MessageType
from protocol.registered_probe import RegisteredProbe
from protocol.registered_modem import RegisteredModem

ProbeID = str
ProbeSocket = socket
ProbeIndex = int
ModemID = str
ModemIndex = int
DeviceIndexer = ProbeID | ProbeSocket | ProbeIndex | ModemID
ModemIndexer = ModemID | ModemIndex


class UnknownDevice:
	"""
	Base class for connected devices.

	Until registration message any connected client is considered as unknown device.
	"""

	def __init__(self, client: socket, address: tuple[str, int], hub: DeviceHub):
		"""
		:param client: connected client socket.
		:param address: tuple of remote (ip, port) of the connected client.
		:param hub: device hub reference.
		"""
		self.hub = hub
		self.socket = client
		self.ip = address[0]
		self.port = address[1]

	@property
	def address(self) -> tuple[str, int]:
		"""
		Client's remote (ip, port) of the connection.
		"""
		return self.ip, self.port

	def register(self, registration_data: zondcom_pb2.Zond_info) -> Probe:
		"""
		Register the device as a probe.

		:param registration_data: registration message of the probe.
		"""
		return Probe(self, registration_data)

	def _update(self, device: UnknownDevice) -> None:
		self.hub = device.hub
		self.socket = device.socket
		self.ip = device.ip
		self.port = device.port


class IConnectable(EventDispatcher):


	def __init__(self, initial_state: bool = True):

		super().__init__()
		self._connection_state = initial_state

	@property
	def is_connected(self) -> bool:
		"""
		Whether the device is currently connected to hub.
		"""
		return self._connection_state

	@property
	def _is_connected(self) -> bool:
		"""
		Whether the device is currently connected to hub.

		Update connection state and trigger corresponding events.
		"""
		# property duplicate to define private setter
		return self.is_connected

	@_is_connected.setter
	def _is_connected(self, state: bool) -> None:
		"""
		Whether the device is currently connected to hub.

		Update connection state and trigger corresponding events.
		"""
		if state == self._connection_state:
			return
		self._connection_state = state
		self._trigger_connection_events(state)

	def _trigger_connection_events(self, state: bool) -> None:
		"""
		Can be overriden to change events logic.

		Called only when state changes.

		:param state: new connection state; old connection state is al;ways inverted.
		"""
		if state:
			self.connect.trigger(self)
		else:
			self.disconnect.trigger(self)

	@event
	def connect(self, device: Self) -> None:
		"""
		The device has recently connected to hub.
		"""
		...

	@event
	def disconnect(self, device: Self) -> None:
		"""
		The device has recently disconnected from hub.
		"""
		...


class Probe(IConnectable, EventDispatcher, RegisteredProbe, UnknownDevice):
	"""
	Registered probe device.
	"""

	def __init__(self, device: UnknownDevice, registration_data: zondcom_pb2.Zond_info):
		"""
		:param device: connected client device.
		:param registration_data: registration message data of the probe.
		"""
		UnknownDevice.__init__(self, device.socket, device.address, device.hub)
		IConnectable.__init__(self)
		EventDispatcher.__init__(self)
		RegisteredProbe.__init__(self)
		self.registration_data = registration_data
		self.modems: list[Modem] = []
		self._register_modems()

	def _register_modems(self, only_ids: set[str] = None):
		self._validate_modems()
		if only_ids is None:
			only_ids = {modem_info.modem_id for modem_info in self.registration_data.modem_info}
		for modem_info in self.registration_data.modem_info:
			if modem_info.modem_id not in only_ids:
				continue
			modem = Modem(self, modem_info)
			self.modems.append(modem)
			self.modem_registered.trigger(modem)

	def _update_modems(self):
		self._validate_modems()
		registered_ids = {modem.id for modem in self}
		current_ids = {modem_info.modem_id for modem_info in self.registration_data.modem_info}
		for id in registered_ids - current_ids:  # disappeared from registration data
			self[id]._is_connected = False
		self._register_modems(only_ids=current_ids - registered_ids)  # new to register
		maybe_update = current_ids & registered_ids  # just change candidates
		for modem_info in self.registration_data.modem_info:
			if modem_info.modem_id in maybe_update:
				self[modem_info.modem_id]._update(modem_info)

	def _validate_modems(self):
		# TODO: Handle errors
		if self.registration_data.modem_num != len(self.registration_data.modem_info):
			print(f'Registered {self.registration_data.modem_num} modems but received {len(self.registration_data.modem_info)} modem descriptors.')
			raise RuntimeError(f'Registered {self.registration_data.modem_num} modems but received {len(self.registration_data.modem_info)} modem descriptors.')
		if len(self.registration_data.modem_info) != len({modem_info.modem_id for modem_info in self.registration_data.modem_info}):
			print('Received duplicated modem id in registration data.')
			raise RuntimeError('Received duplicated modem id in registration data.')

	def __iter__(self) -> Iterator[Modem]:
		return iter(self.modems)

	def __len__(self) -> int:
		return len(self.modems)

	def __getitem__(self, item: ModemIndexer) -> Modem | None:
		"""
		Get bound modem by id or index.
		"""
		for i, modem in enumerate(self):
			if modem.id == item or item == i:
				return modem

	@event
	def modem_registered(self, modem: Modem) -> None:
		"""
		New modem registered on the probe.

		:param modem: registered modem.
		"""
		...

	@event
	def telemetry_received(self, data: zondcom_pb2.Zond_metrics, probe: Probe) -> None:
		"""
		Telemetry from probe was received.
		"""
		pass

	@event
	def connect(self, probe: Probe) -> None:
		"""
		The probe has recently connected to hub.

		When probe connects all modems' connection state stay unchanged but may trigger connection events.
		"""
		...

	@event
	def updated(self, probe: Probe) -> None:
		"""
		Occurs when probe, modem or underlying socket was updated.
		"""
		...

	@event
	def disconnect(self, probe: Probe) -> None:
		"""
		The probe has recently disconnected from hub.

		When probe disconnects all modems disconnect too.
		"""
		...

	async def send_directive(self, directive: str, **directive_args) -> str | None:
		"""
		Send directive.

		:param directive: directive command.
		:param directive_args: directive command args.
		"""
		return await self.hub._send_directive(self.socket, directive, directive_args)

	def _update(self, registration_data: zondcom_pb2.Zond_info, *, device: UnknownDevice | None = None, connected: bool = True) -> None:
		"""
		Update probe data. Recursively update nested modems. Set connected state.
		"""
		if device is not None:
			UnknownDevice._update(self, device)
		has_changed = registration_data != self.registration_data
		if has_changed:
			self.registration_data = registration_data
		self._update_modems()
		self._is_connected = connected
		if has_changed or device is not None:
			self.updated.trigger(self)


class Modem(IConnectable, RegisteredModem, EventDispatcher):
	"""
	Registered modem device bound to a probe.
	"""

	def __init__(self, probe: Probe, registration_data: zondcom_pb2.Modem_info):
		"""
		:param probe: connected probe to bind the modem to.
		:param registration_data: registration message data of the modem.
		"""
		IConnectable.__init__(self)
		RegisteredProbe.__init__(self)
		EventDispatcher.__init__(self)
		self.probe = probe
		self.registration_data = registration_data
		self._last_connection_state = self.is_connected  # Can be overwritten without this flag, but I am too lazy.
		self._pending_connection_event = False
		probe.connect(self._on_probe_connected)
		probe.disconnect(self._on_probe_disconnected)

	def _on_probe_connected(self, probe: Probe) -> None:
		if self._pending_connection_event:
			if not self.is_connected:  # Consider never will be True but add for safety.
				self._is_connected = True
			else:
				self.connect.trigger(self)
		else:
			self._is_connected = self._last_connection_state

	def _on_probe_disconnected(self, probe: Probe) -> None:
		self._last_connection_state = self.is_connected
		self._is_connected = False

	def _trigger_connection_events(self, state: bool) -> None:
		# Fire events conditionally related to probe connection state.
		if state:
			if self.probe.is_connected:
				self.connect.trigger(self)
			else:
				self._pending_connection_event = True
		else:
			self.disconnect.trigger(self)

	@event
	def telemetry_received(self, data: zondcom_pb2.Modem_metrics, modem: Modem) -> None:
		"""
		Telemetry from modem was received.
		"""
		pass

	@event
	def connect(self, modem: Modem) -> None:
		"""
		The modem has recently connected to hub or probe.

		When probe connects all modems' connection state stay unchanged but may trigger connection events.
		"""
		...

	@event
	def disconnect(self, modem: Modem) -> None:
		"""
		The modem has recently disconnected from hub or probe.

		When probe disconnects all modems disconnect too.
		"""
		...

	@event
	def updated(self, modem: Modem) -> None:
		"""
		Occurs when  modem was updated.
		"""
		...

	async def send_directive(self, directive: str, **directive_args) -> str | None:
		"""
		Send directive.

		:param directive: directive command.
		:param directive_args: directive command args.
		"""
		return await self.probe.hub._send_directive(self.probe.socket, directive, directive_args, modem=self)

	def _update(self, registration_data: zondcom_pb2.Modem_info, *, connected: bool = True) -> None:
		"""
		Update modem data. Set connected state.
		"""
		has_changed = registration_data != self.registration_data
		if has_changed:
			self.registration_data = registration_data
		self._is_connected = connected
		if has_changed:
			self.updated.trigger(self)


class PendingDirective:
	"""
	Internal class representing pending directive.
	"""

	def __init__(self):
		self.id = str(uuid.uuid4())
		self.response: str | None = None
		self._lock = asyncio.Event()

	@property
	def resolved(self) -> bool:
		"""
		Whether response has been received.
		"""
		return self._lock.is_set()

	def resolve(self, response: str | None) -> None:
		"""
		Resolve directive with received response.

		:param response: received response data.
		"""
		if not self.resolved:
			self.response = response
			self._lock.set()

	async def wait(self) -> str:
		"""
		Wait until directive response is received and return it.
		"""
		await self._lock.wait()
		return self.response

	def resolve_timeout(self, timeout: float, *, loop: asyncio.AbstractEventLoop | None = None) -> asyncio.Task:
		"""
		Create background task to resolve the directive by timeout if no response will have been received.
		"""
		if loop is None:
			loop = asyncio.get_event_loop()
		return loop.create_task(self._resolve_timeout(timeout))

	async def _resolve_timeout(self, timeout: float) -> None:
		await asyncio.sleep(timeout)
		self.resolve(None)


class DeviceHub(EventDispatcher):
	"""
	Manager of connected devices.
	"""

	def __init__(self, transport: ITransport | None = None, timeout: float = 30):
		"""
		:param transport: attach to underlying transport layer that actually manages socket connections and routing. If None no attachment is done at construction. Anyway transport must be attached before probe manager utilization.
		"""
		super().__init__()
		self.timeout = timeout
		self._pending_directives: dict[str, PendingDirective] = {}
		self._unknown_devices: list[UnknownDevice] = []
		self._registered_probes: list[Probe] = []
		self.transport: ITransport | None = None
		if transport is not None:
			self.attach(transport)

	def __getitem__(self, item: DeviceIndexer) -> Probe | Modem | None:
		"""
		Get registered probe by id or client socket or device index in hub.

		Get registered modem by id.
		"""
		for i, probe in enumerate(self):
			if isinstance(item, socket) and probe.socket is item or probe.id == item or item == i:
				return probe
		for probe in self:
			for modem in probe:
				if modem.id == item or modem.imsi == item:
					return modem

	def __len__(self) -> int:
		"""
		Get registered devices count.
		"""
		return len(self._registered_probes)

	def __iter__(self) -> Iterator[Probe]:
		"""
		Iterate over registered devices.
		"""
		return iter(self._registered_probes)

	def _get_unknown_device(self, client: socket) -> UnknownDevice | None:
		"""
		Get unknown device.

		:param client: client socket.
		"""
		for device in self._unknown_devices:
			if device.socket is client:
				return device

	def _on_socket_connected(self, client: socket, address: tuple[str, int]) -> None:
		"""
		Handles socket connection to attached transport layer.

		:param client: the connected socket.
		:param address: tuple of remote (ip, port) of the connected client.
		"""
		self._on_socket_disconnected(client, optional=True)
		self._unknown_devices.append(UnknownDevice(client, address, self))

	def _on_socket_disconnected(self, client: socket, *, optional: bool = False) -> None:
		"""
		Handles socket disconnection from attached transport layer.

		:param client: the disconnected socket.
		:param optional: for manual call: do not rise error if client is not presented in the hub.
		"""
		found = False
		for device in self._unknown_devices.copy():
			if device.socket is client:
				self._unknown_devices.remove(device)
				found = True
		if (probe := self[client]) is not None:
			probe._is_connected = False
			found = True
		if not found and not optional:
			# TODO: Handle error
			print('[WARNING]', 'Disconnected client is not presented in the device hub.', client)

	def _on_message_received(self, client: socket, message: zondcom_pb2.Protocol, message_type: MessageType) -> None:
		"""
		Handles new message from connected socket.

		:param client: the socket the message received from.
		:param message: the received message.
		:param message_type: type of received message.
		"""
		# TODO: implement message handlers
		match message_type:
			case MessageType.Registration:
				if (probe := self[client]) is not None:
					probe._update(message.zond_info)
				elif (unknown_device := self._get_unknown_device(client)) is not None:
					if (probe := self[message.zond_info.zond_id]) is not None:
						probe._update(message.zond_info, device=unknown_device)
					else:
						self._register_probe(unknown_device, message)
				else:
					# TODO: Handle error
					print('[WARNING]', 'Unknown device registration received', client, message)
			case MessageType.DirectiveResponse:
				if message.directive_response.msg_id in self._pending_directives:
					self._pending_directives[message.directive_response.msg_id].resolve(message.directive_response.response)
				else:
					# TODO: Handle error
					print('[WARNING]', 'Unknown directive response', client, message)
			case MessageType.ZondMetrics:
				if (probe := self[message.zond_metrics.zond_id]) is None or not isinstance(probe, Probe):
					# TODO: Handle error
					print('[WARNING]', 'Unknown probe device telemetry received', client, message)
				else:
					probe.telemetry_received.trigger(message.zond_metrics, probe)
			case MessageType.ModemMetrics:
				if (modem := self[message.modem_metrics.modem_id]) is None or not isinstance(modem, Modem):
					# TODO: Handle error
					print('[WARNING]', 'Unknown modem device telemetry received', client, message)
				else:
					modem.telemetry_received.trigger(message.modem_metrics, modem)

	def _register_probe(self, device: UnknownDevice, registration_message: zondcom_pb2.Protocol) -> Probe:
		probe = device.register(registration_message.zond_info)
		self._unknown_devices.remove(device)
		self._registered_probes.append(probe)

		@probe.modem_registered
		def on_modem_registered(modem: Modem) -> None:
			self.modem_registered.trigger(modem)

		self.probe_registered.trigger(probe)
		[self.modem_registered.trigger(modem) for modem in probe.modems]
		return probe

	async def _send_directive(self, client: socket, directive: str, directive_args: dict, modem: Modem | None = None) -> str | None:
		promise = PendingDirective()
		self._pending_directives[promise.id] = promise
		self.transport.send_directive(client, directive, directive_args, promise.id, modem_id=modem.id if modem else '')
		promise.resolve_timeout(self.timeout)
		response = await promise.wait()
		del self._pending_directives[promise.id]
		return response

	def attach(self, transport: ITransport) -> None:
		"""
		Attach to specified underlying transport layer.

		:param transport: underlying transport layer that actually manages socket connections and routing. If specified in constructor automatically attached during initialization.
		"""
		self.transport = transport
		# TODO: Handle client deregistration
		transport.socket_disconnected(self._on_socket_disconnected)
		transport.message_received(self._on_message_received)
		transport.socket_connected(self._on_socket_connected)

	@event
	def probe_registered(self, probe: Probe) -> None:
		"""
		New probe registered in the hub.

		:param probe: registered probe.
		"""
		...

	@event
	def modem_registered(self, modem: Modem) -> None:
		"""
		New modem registered on some probe in the hub.

		:param modem: registered modem.
		"""
		...
