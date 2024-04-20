from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlerCls:
	"""Bler commands group definition. 21 total commands, 8 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bler", core, parent)

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_throughput'):
			from .Throughput import ThroughputCls
			self._throughput = ThroughputCls(self._core, self._cmd_group)
		return self._throughput

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	@property
	def cword(self):
		"""cword commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cword'):
			from .Cword import CwordCls
			self._cword = CwordCls(self._core, self._cmd_group)
		return self._cword

	@property
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_confidence'):
			from .Confidence import ConfidenceCls
			self._confidence = ConfidenceCls(self._core, self._cmd_group)
		return self._confidence

	@property
	def overall(self):
		"""overall commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_overall'):
			from .Overall import OverallCls
			self._overall = OverallCls(self._core, self._cmd_group)
		return self._overall

	@property
	def uplink(self):
		"""uplink commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def abort(self) -> None:
		"""SCPI: ABORt:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.abort() \n
		Stops the measurement. The measurement enters the 'RDY' state. \n
		"""
		self._core.io.write(f'ABORt:SIGNaling:MEASurement:BLER')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.abort_with_opc() \n
		Stops the measurement. The measurement enters the 'RDY' state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:SIGNaling:MEASurement:BLER', opc_timeout_ms)

	def stop(self) -> None:
		"""SCPI: STOP:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:SIGNaling:MEASurement:BLER')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:SIGNaling:MEASurement:BLER', opc_timeout_ms)

	def initiate(self) -> None:
		"""SCPI: INITiate:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.initiate() \n
		Starts the measurement. The measurement enters the 'RUN' state. \n
		"""
		self._core.io.write(f'INITiate:SIGNaling:MEASurement:BLER')

	def initiate_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:SIGNaling:MEASurement:BLER \n
		Snippet: driver.signaling.measurement.bler.initiate_with_opc() \n
		Starts the measurement. The measurement enters the 'RUN' state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:SIGNaling:MEASurement:BLER', opc_timeout_ms)

	def clone(self) -> 'BlerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BlerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
