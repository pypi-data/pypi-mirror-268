from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCls:
	"""Ue commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ue", core, parent)

	@property
	def dcMode(self):
		"""dcMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcMode'):
			from .DcMode import DcModeCls
			self._dcMode = DcModeCls(self._core, self._cmd_group)
		return self._dcMode

	@property
	def rcid(self):
		"""rcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcid'):
			from .Rcid import RcidCls
			self._rcid = RcidCls(self._core, self._cmd_group)
		return self._rcid

	@property
	def rrcState(self):
		"""rrcState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrcState'):
			from .RrcState import RrcStateCls
			self._rrcState = RrcStateCls(self._core, self._cmd_group)
		return self._rrcState

	@property
	def imei(self):
		"""imei commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imei'):
			from .Imei import ImeiCls
			self._imei = ImeiCls(self._core, self._cmd_group)
		return self._imei

	@property
	def imsi(self):
		"""imsi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imsi'):
			from .Imsi import ImsiCls
			self._imsi = ImsiCls(self._core, self._cmd_group)
		return self._imsi

	def clone(self) -> 'UeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
