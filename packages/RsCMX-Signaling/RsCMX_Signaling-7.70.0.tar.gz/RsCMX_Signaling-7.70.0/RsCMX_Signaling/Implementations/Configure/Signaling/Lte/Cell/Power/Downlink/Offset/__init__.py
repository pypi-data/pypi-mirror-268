from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	@property
	def pss(self):
		"""pss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pss'):
			from .Pss import PssCls
			self._pss = PssCls(self._core, self._cmd_group)
		return self._pss

	@property
	def sss(self):
		"""sss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sss'):
			from .Sss import SssCls
			self._sss = SssCls(self._core, self._cmd_group)
		return self._sss

	@property
	def rs(self):
		"""rs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rs'):
			from .Rs import RsCls
			self._rs = RsCls(self._core, self._cmd_group)
		return self._rs

	@property
	def pbch(self):
		"""pbch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbch'):
			from .Pbch import PbchCls
			self._pbch = PbchCls(self._core, self._cmd_group)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcfich'):
			from .Pcfich import PcfichCls
			self._pcfich = PcfichCls(self._core, self._cmd_group)
		return self._pcfich

	@property
	def pdcch(self):
		"""pdcch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import PdcchCls
			self._pdcch = PdcchCls(self._core, self._cmd_group)
		return self._pdcch

	def clone(self) -> 'OffsetCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OffsetCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
