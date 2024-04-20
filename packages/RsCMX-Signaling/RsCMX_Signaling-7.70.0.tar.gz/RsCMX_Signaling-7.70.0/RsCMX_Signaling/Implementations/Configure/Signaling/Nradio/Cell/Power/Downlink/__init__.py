from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 15 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def sepre(self):
		"""sepre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sepre'):
			from .Sepre import SepreCls
			self._sepre = SepreCls(self._core, self._cmd_group)
		return self._sepre

	@property
	def tcell(self):
		"""tcell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcell'):
			from .Tcell import TcellCls
			self._tcell = TcellCls(self._core, self._cmd_group)
		return self._tcell

	@property
	def pppScaling(self):
		"""pppScaling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pppScaling'):
			from .PppScaling import PppScalingCls
			self._pppScaling = PppScalingCls(self._core, self._cmd_group)
		return self._pppScaling

	@property
	def poffset(self):
		"""poffset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import PoffsetCls
			self._poffset = PoffsetCls(self._core, self._cmd_group)
		return self._poffset

	@property
	def ocng(self):
		"""ocng commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ocng'):
			from .Ocng import OcngCls
			self._ocng = OcngCls(self._core, self._cmd_group)
		return self._ocng

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
