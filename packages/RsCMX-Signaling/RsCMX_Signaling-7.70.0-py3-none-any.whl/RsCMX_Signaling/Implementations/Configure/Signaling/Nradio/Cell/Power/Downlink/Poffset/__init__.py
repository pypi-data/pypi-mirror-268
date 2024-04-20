from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoffsetCls:
	"""Poffset commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	@property
	def ssb(self):
		"""ssb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssb'):
			from .Ssb import SsbCls
			self._ssb = SsbCls(self._core, self._cmd_group)
		return self._ssb

	@property
	def pss(self):
		"""pss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pss'):
			from .Pss import PssCls
			self._pss = PssCls(self._core, self._cmd_group)
		return self._pss

	@property
	def coreset(self):
		"""coreset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coreset'):
			from .Coreset import CoresetCls
			self._coreset = CoresetCls(self._core, self._cmd_group)
		return self._coreset

	@property
	def nrDl(self):
		"""nrDl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrDl'):
			from .NrDl import NrDlCls
			self._nrDl = NrDlCls(self._core, self._cmd_group)
		return self._nrDl

	def clone(self) -> 'PoffsetCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PoffsetCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
