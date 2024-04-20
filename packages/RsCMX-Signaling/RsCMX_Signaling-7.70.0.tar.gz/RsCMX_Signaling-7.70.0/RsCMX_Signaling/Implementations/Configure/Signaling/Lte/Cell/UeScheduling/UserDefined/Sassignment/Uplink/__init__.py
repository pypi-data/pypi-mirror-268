from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 10 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def pdcchFormat(self):
		"""pdcchFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcchFormat'):
			from .PdcchFormat import PdcchFormatCls
			self._pdcchFormat = PdcchFormatCls(self._core, self._cmd_group)
		return self._pdcchFormat

	@property
	def dciFormat(self):
		"""dciFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dciFormat'):
			from .DciFormat import DciFormatCls
			self._dciFormat = DciFormatCls(self._core, self._cmd_group)
		return self._dciFormat

	@property
	def riv(self):
		"""riv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_riv'):
			from .Riv import RivCls
			self._riv = RivCls(self._core, self._cmd_group)
		return self._riv

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Rb import RbCls
			self._rb = RbCls(self._core, self._cmd_group)
		return self._rb

	@property
	def cword(self):
		"""cword commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cword'):
			from .Cword import CwordCls
			self._cword = CwordCls(self._core, self._cmd_group)
		return self._cword

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
