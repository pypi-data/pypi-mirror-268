from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RburstCls:
	"""Rburst commands group definition. 8 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rburst", core, parent)

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
	def plSubframe(self):
		"""plSubframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plSubframe'):
			from .PlSubframe import PlSubframeCls
			self._plSubframe = PlSubframeCls(self._core, self._cmd_group)
		return self._plSubframe

	@property
	def btProb(self):
		"""btProb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_btProb'):
			from .BtProb import BtProbCls
			self._btProb = BtProbCls(self._core, self._cmd_group)
		return self._btProb

	@property
	def ipsProb(self):
		"""ipsProb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipsProb'):
			from .IpsProb import IpsProbCls
			self._ipsProb = IpsProbCls(self._core, self._cmd_group)
		return self._ipsProb

	@property
	def ccrnti(self):
		"""ccrnti commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccrnti'):
			from .Ccrnti import CcrntiCls
			self._ccrnti = CcrntiCls(self._core, self._cmd_group)
		return self._ccrnti

	def clone(self) -> 'RburstCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RburstCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
