from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigureCls:
	"""Configure commands group definition. 903 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def signaling(self):
		"""signaling commands group. 16 Sub-classes, 3 commands."""
		if not hasattr(self, '_signaling'):
			from .Signaling import SignalingCls
			self._signaling = SignalingCls(self._core, self._cmd_group)
		return self._signaling

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def nrSub(self):
		"""nrSub commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrSub'):
			from .NrSub import NrSubCls
			self._nrSub = NrSubCls(self._core, self._cmd_group)
		return self._nrSub

	@property
	def nrMmw(self):
		"""nrMmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrMmw'):
			from .NrMmw import NrMmwCls
			self._nrMmw = NrMmwCls(self._core, self._cmd_group)
		return self._nrMmw

	@property
	def wlan(self):
		"""wlan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wlan'):
			from .Wlan import WlanCls
			self._wlan = WlanCls(self._core, self._cmd_group)
		return self._wlan

	def clone(self) -> 'ConfigureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ConfigureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
