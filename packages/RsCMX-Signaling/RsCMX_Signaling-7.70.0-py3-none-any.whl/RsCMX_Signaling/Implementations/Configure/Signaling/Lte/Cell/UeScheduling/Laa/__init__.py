from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LaaCls:
	"""Laa commands group definition. 28 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("laa", core, parent)

	@property
	def tbursts(self):
		"""tbursts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbursts'):
			from .Tbursts import TburstsCls
			self._tbursts = TburstsCls(self._core, self._cmd_group)
		return self._tbursts

	@property
	def fburst(self):
		"""fburst commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_fburst'):
			from .Fburst import FburstCls
			self._fburst = FburstCls(self._core, self._cmd_group)
		return self._fburst

	@property
	def rburst(self):
		"""rburst commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_rburst'):
			from .Rburst import RburstCls
			self._rburst = RburstCls(self._core, self._cmd_group)
		return self._rburst

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
		"""cword commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cword'):
			from .Cword import CwordCls
			self._cword = CwordCls(self._core, self._cmd_group)
		return self._cword

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import CrateCls
			self._crate = CrateCls(self._core, self._cmd_group)
		return self._crate

	@property
	def csat(self):
		"""csat commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_csat'):
			from .Csat import CsatCls
			self._csat = CsatCls(self._core, self._cmd_group)
		return self._csat

	def clone(self) -> 'LaaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LaaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
