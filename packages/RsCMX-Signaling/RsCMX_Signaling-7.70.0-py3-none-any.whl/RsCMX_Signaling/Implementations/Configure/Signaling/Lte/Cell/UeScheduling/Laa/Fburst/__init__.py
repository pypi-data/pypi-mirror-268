from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FburstCls:
	"""Fburst commands group definition. 8 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fburst", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def pbtr(self):
		"""pbtr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbtr'):
			from .Pbtr import PbtrCls
			self._pbtr = PbtrCls(self._core, self._cmd_group)
		return self._pbtr

	@property
	def blength(self):
		"""blength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blength'):
			from .Blength import BlengthCls
			self._blength = BlengthCls(self._core, self._cmd_group)
		return self._blength

	@property
	def fsBurst(self):
		"""fsBurst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsBurst'):
			from .FsBurst import FsBurstCls
			self._fsBurst = FsBurstCls(self._core, self._cmd_group)
		return self._fsBurst

	@property
	def isaBurst(self):
		"""isaBurst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isaBurst'):
			from .IsaBurst import IsaBurstCls
			self._isaBurst = IsaBurstCls(self._core, self._cmd_group)
		return self._isaBurst

	@property
	def oslSubframe(self):
		"""oslSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oslSubframe'):
			from .OslSubframe import OslSubframeCls
			self._oslSubframe = OslSubframeCls(self._core, self._cmd_group)
		return self._oslSubframe

	@property
	def ccrnti(self):
		"""ccrnti commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccrnti'):
			from .Ccrnti import CcrntiCls
			self._ccrnti = CcrntiCls(self._core, self._cmd_group)
		return self._ccrnti

	def clone(self) -> 'FburstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FburstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
