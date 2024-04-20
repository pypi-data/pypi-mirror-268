from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CnCodebookCls:
	"""CnCodebook commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnCodebook", core, parent)

	@property
	def tdBehavior(self):
		"""tdBehavior commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdBehavior'):
			from .TdBehavior import TdBehaviorCls
			self._tdBehavior = TdBehaviorCls(self._core, self._cmd_group)
		return self._tdBehavior

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import UsageCls
			self._usage = UsageCls(self._core, self._cmd_group)
		return self._usage

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def resource(self):
		"""resource commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_resource'):
			from .Resource import ResourceCls
			self._resource = ResourceCls(self._core, self._cmd_group)
		return self._resource

	@property
	def scheduler(self):
		"""scheduler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scheduler'):
			from .Scheduler import SchedulerCls
			self._scheduler = SchedulerCls(self._core, self._cmd_group)
		return self._scheduler

	def clone(self) -> 'CnCodebookCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CnCodebookCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
