from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimingCls:
	"""Timing commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import OffsetCls
			self._offset = OffsetCls(self._core, self._cmd_group)
		return self._offset

	@property
	def sfnOffset(self):
		"""sfnOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfnOffset'):
			from .SfnOffset import SfnOffsetCls
			self._sfnOffset = SfnOffsetCls(self._core, self._cmd_group)
		return self._sfnOffset

	@property
	def dltShift(self):
		"""dltShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dltShift'):
			from .DltShift import DltShiftCls
			self._dltShift = DltShiftCls(self._core, self._cmd_group)
		return self._dltShift

	def clone(self) -> 'TimingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
