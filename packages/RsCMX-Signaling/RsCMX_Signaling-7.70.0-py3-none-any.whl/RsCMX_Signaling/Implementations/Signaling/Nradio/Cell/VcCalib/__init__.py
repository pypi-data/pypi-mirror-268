from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VcCalibCls:
	"""VcCalib commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vcCalib", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def isolation(self):
		"""isolation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_isolation'):
			from .Isolation import IsolationCls
			self._isolation = IsolationCls(self._core, self._cmd_group)
		return self._isolation

	@property
	def matrix(self):
		"""matrix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_matrix'):
			from .Matrix import MatrixCls
			self._matrix = MatrixCls(self._core, self._cmd_group)
		return self._matrix

	@property
	def iquality(self):
		"""iquality commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iquality'):
			from .Iquality import IqualityCls
			self._iquality = IqualityCls(self._core, self._cmd_group)
		return self._iquality

	@property
	def branch(self):
		"""branch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_branch'):
			from .Branch import BranchCls
			self._branch = BranchCls(self._core, self._cmd_group)
		return self._branch

	def clone(self) -> 'VcCalibCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VcCalibCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
