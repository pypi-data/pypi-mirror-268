from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 14 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def rcMode(self):
		"""rcMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcMode'):
			from .RcMode import RcModeCls
			self._rcMode = RcModeCls(self._core, self._cmd_group)
		return self._rcMode

	@property
	def meRms(self):
		"""meRms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_meRms'):
			from .MeRms import MeRmsCls
			self._meRms = MeRmsCls(self._core, self._cmd_group)
		return self._meRms

	@property
	def meepre(self):
		"""meepre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_meepre'):
			from .Meepre import MeepreCls
			self._meepre = MeepreCls(self._core, self._cmd_group)
		return self._meepre

	@property
	def auto(self):
		"""auto commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def prStep(self):
		"""prStep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prStep'):
			from .PrStep import PrStepCls
			self._prStep = PrStepCls(self._core, self._cmd_group)
		return self._prStep

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Cindex import CindexCls
			self._cindex = CindexCls(self._core, self._cmd_group)
		return self._cindex

	@property
	def prtPower(self):
		"""prtPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prtPower'):
			from .PrtPower import PrtPowerCls
			self._prtPower = PrtPowerCls(self._core, self._cmd_group)
		return self._prtPower

	@property
	def lrsIndex(self):
		"""lrsIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrsIndex'):
			from .LrsIndex import LrsIndexCls
			self._lrsIndex = LrsIndexCls(self._core, self._cmd_group)
		return self._lrsIndex

	@property
	def zczConfig(self):
		"""zczConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zczConfig'):
			from .ZczConfig import ZczConfigCls
			self._zczConfig = ZczConfigCls(self._core, self._cmd_group)
		return self._zczConfig

	@property
	def ipPreambles(self):
		"""ipPreambles commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipPreambles'):
			from .IpPreambles import IpPreamblesCls
			self._ipPreambles = IpPreamblesCls(self._core, self._cmd_group)
		return self._ipPreambles

	@property
	def redCap(self):
		"""redCap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_redCap'):
			from .RedCap import RedCapCls
			self._redCap = RedCapCls(self._core, self._cmd_group)
		return self._redCap

	@property
	def spreambles(self):
		"""spreambles commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spreambles'):
			from .Spreambles import SpreamblesCls
			self._spreambles = SpreamblesCls(self._core, self._cmd_group)
		return self._spreambles

	@property
	def npreambles(self):
		"""npreambles commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npreambles'):
			from .Npreambles import NpreamblesCls
			self._npreambles = NpreamblesCls(self._core, self._cmd_group)
		return self._npreambles

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
