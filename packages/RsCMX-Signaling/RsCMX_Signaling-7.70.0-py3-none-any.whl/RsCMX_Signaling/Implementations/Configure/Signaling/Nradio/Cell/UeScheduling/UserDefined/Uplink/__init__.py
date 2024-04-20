from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def bpid(self):
		"""bpid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bpid'):
			from .Bpid import BpidCls
			self._bpid = BpidCls(self._core, self._cmd_group)
		return self._bpid

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import AlevelCls
			self._alevel = AlevelCls(self._core, self._cmd_group)
		return self._alevel

	@property
	def ssid(self):
		"""ssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssid'):
			from .Ssid import SsidCls
			self._ssid = SsidCls(self._core, self._cmd_group)
		return self._ssid

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def paFactor(self):
		"""paFactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paFactor'):
			from .PaFactor import PaFactorCls
			self._paFactor = PaFactorCls(self._core, self._cmd_group)
		return self._paFactor

	@property
	def prtype(self):
		"""prtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prtype'):
			from .Prtype import PrtypeCls
			self._prtype = PrtypeCls(self._core, self._cmd_group)
		return self._prtype

	@property
	def pnoRepet(self):
		"""pnoRepet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnoRepet'):
			from .PnoRepet import PnoRepetCls
			self._pnoRepet = PnoRepetCls(self._core, self._cmd_group)
		return self._pnoRepet

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
