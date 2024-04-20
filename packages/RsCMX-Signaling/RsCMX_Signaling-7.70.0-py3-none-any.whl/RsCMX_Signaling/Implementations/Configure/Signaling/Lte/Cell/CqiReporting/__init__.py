from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CqiReportingCls:
	"""CqiReporting commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqiReporting", core, parent)

	@property
	def rtype(self):
		"""rtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtype'):
			from .Rtype import RtypeCls
			self._rtype = RtypeCls(self._core, self._cmd_group)
		return self._rtype

	@property
	def findicator(self):
		"""findicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_findicator'):
			from .Findicator import FindicatorCls
			self._findicator = FindicatorCls(self._core, self._cmd_group)
		return self._findicator

	@property
	def rmode(self):
		"""rmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmode'):
			from .Rmode import RmodeCls
			self._rmode = RmodeCls(self._core, self._cmd_group)
		return self._rmode

	@property
	def sancqi(self):
		"""sancqi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sancqi'):
			from .Sancqi import SancqiCls
			self._sancqi = SancqiCls(self._core, self._cmd_group)
		return self._sancqi

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Cindex import CindexCls
			self._cindex = CindexCls(self._core, self._cmd_group)
		return self._cindex

	@property
	def prEnable(self):
		"""prEnable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prEnable'):
			from .PrEnable import PrEnableCls
			self._prEnable = PrEnableCls(self._core, self._cmd_group)
		return self._prEnable

	def clone(self) -> 'CqiReportingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CqiReportingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
