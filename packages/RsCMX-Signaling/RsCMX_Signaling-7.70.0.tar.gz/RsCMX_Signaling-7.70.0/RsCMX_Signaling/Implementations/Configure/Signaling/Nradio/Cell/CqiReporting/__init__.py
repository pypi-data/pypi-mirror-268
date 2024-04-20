from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CqiReportingCls:
	"""CqiReporting commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqiReporting", core, parent)

	@property
	def combined(self):
		"""combined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_combined'):
			from .Combined import CombinedCls
			self._combined = CombinedCls(self._core, self._cmd_group)
		return self._combined

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def periodicity(self):
		"""periodicity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_periodicity'):
			from .Periodicity import PeriodicityCls
			self._periodicity = PeriodicityCls(self._core, self._cmd_group)
		return self._periodicity

	@property
	def resource(self):
		"""resource commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_resource'):
			from .Resource import ResourceCls
			self._resource = ResourceCls(self._core, self._cmd_group)
		return self._resource

	@property
	def report(self):
		"""report commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_report'):
			from .Report import ReportCls
			self._report = ReportCls(self._core, self._cmd_group)
		return self._report

	def clone(self) -> 'CqiReportingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CqiReportingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
