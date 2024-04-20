from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReSelectionCls:
	"""ReSelection commands group definition. 11 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reSelection", core, parent)

	@property
	def common(self):
		"""common commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_common'):
			from .Common import CommonCls
			self._common = CommonCls(self._core, self._cmd_group)
		return self._common

	@property
	def search(self):
		"""search commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_search'):
			from .Search import SearchCls
			self._search = SearchCls(self._core, self._cmd_group)
		return self._search

	@property
	def thresholds(self):
		"""thresholds commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_thresholds'):
			from .Thresholds import ThresholdsCls
			self._thresholds = ThresholdsCls(self._core, self._cmd_group)
		return self._thresholds

	@property
	def minLevel(self):
		"""minLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minLevel'):
			from .MinLevel import MinLevelCls
			self._minLevel = MinLevelCls(self._core, self._cmd_group)
		return self._minLevel

	@property
	def priority(self):
		"""priority commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_priority'):
			from .Priority import PriorityCls
			self._priority = PriorityCls(self._core, self._cmd_group)
		return self._priority

	@property
	def timer(self):
		"""timer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timer'):
			from .Timer import TimerCls
			self._timer = TimerCls(self._core, self._cmd_group)
		return self._timer

	def clone(self) -> 'ReSelectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReSelectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
