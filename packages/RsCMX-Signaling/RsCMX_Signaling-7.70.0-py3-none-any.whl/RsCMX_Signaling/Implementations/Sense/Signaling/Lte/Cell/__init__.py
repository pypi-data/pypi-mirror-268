from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 6 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def bbgIndex(self):
		"""bbgIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbgIndex'):
			from .BbgIndex import BbgIndexCls
			self._bbgIndex = BbgIndexCls(self._core, self._cmd_group)
		return self._bbgIndex

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .UeScheduling import UeSchedulingCls
			self._ueScheduling = UeSchedulingCls(self._core, self._cmd_group)
		return self._ueScheduling

	@property
	def harq(self):
		"""harq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import HarqCls
			self._harq = HarqCls(self._core, self._cmd_group)
		return self._harq

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
