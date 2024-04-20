from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 17 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def ueReport(self):
		"""ueReport commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_ueReport'):
			from .UeReport import UeReportCls
			self._ueReport = UeReportCls(self._core, self._cmd_group)
		return self._ueReport

	@property
	def bler(self):
		"""bler commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_bler'):
			from .Bler import BlerCls
			self._bler = BlerCls(self._core, self._cmd_group)
		return self._bler

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
