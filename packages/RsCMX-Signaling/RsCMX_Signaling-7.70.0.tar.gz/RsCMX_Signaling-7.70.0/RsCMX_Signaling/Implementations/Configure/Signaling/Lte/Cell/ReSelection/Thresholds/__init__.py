from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThresholdsCls:
	"""Thresholds commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thresholds", core, parent)

	@property
	def lowp(self):
		"""lowp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lowp'):
			from .Lowp import LowpCls
			self._lowp = LowpCls(self._core, self._cmd_group)
		return self._lowp

	@property
	def lowq(self):
		"""lowq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lowq'):
			from .Lowq import LowqCls
			self._lowq = LowqCls(self._core, self._cmd_group)
		return self._lowq

	@property
	def higHq(self):
		"""higHq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_higHq'):
			from .HigHq import HigHqCls
			self._higHq = HigHqCls(self._core, self._cmd_group)
		return self._higHq

	def clone(self) -> 'ThresholdsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ThresholdsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
