from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def sfInterval(self):
		"""sfInterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfInterval'):
			from .SfInterval import SfIntervalCls
			self._sfInterval = SfIntervalCls(self._core, self._cmd_group)
		return self._sfInterval

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Rb import RbCls
			self._rb = RbCls(self._core, self._cmd_group)
		return self._rb

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def tbsBits(self):
		"""tbsBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsBits'):
			from .TbsBits import TbsBitsCls
			self._tbsBits = TbsBitsCls(self._core, self._cmd_group)
		return self._tbsBits

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
