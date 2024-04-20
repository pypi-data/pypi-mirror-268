from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 9 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def bwp(self):
		"""bwp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwp'):
			from .Bwp import BwpCls
			self._bwp = BwpCls(self._core, self._cmd_group)
		return self._bwp

	@property
	def cmatrix(self):
		"""cmatrix commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Cmatrix import CmatrixCls
			self._cmatrix = CmatrixCls(self._core, self._cmd_group)
		return self._cmatrix

	@property
	def vcCalib(self):
		"""vcCalib commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_vcCalib'):
			from .VcCalib import VcCalibCls
			self._vcCalib = VcCalibCls(self._core, self._cmd_group)
		return self._vcCalib

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
