from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 20 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def cmode(self):
		"""cmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmode'):
			from .Cmode import CmodeCls
			self._cmode = CmodeCls(self._core, self._cmd_group)
		return self._cmode

	@property
	def epre(self):
		"""epre commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epre'):
			from .Epre import EpreCls
			self._epre = EpreCls(self._core, self._cmd_group)
		return self._epre

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import RmsCls
			self._rms = RmsCls(self._core, self._cmd_group)
		return self._rms

	@property
	def auto(self):
		"""auto commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def fcoefficient(self):
		"""fcoefficient commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcoefficient'):
			from .Fcoefficient import FcoefficientCls
			self._fcoefficient = FcoefficientCls(self._core, self._cmd_group)
		return self._fcoefficient

	@property
	def psRsOffset(self):
		"""psRsOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psRsOffset'):
			from .PsRsOffset import PsRsOffsetCls
			self._psRsOffset = PsRsOffsetCls(self._core, self._cmd_group)
		return self._psRsOffset

	@property
	def alpha(self):
		"""alpha commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alpha'):
			from .Alpha import AlphaCls
			self._alpha = AlphaCls(self._core, self._cmd_group)
		return self._alpha

	@property
	def pmax(self):
		"""pmax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmax'):
			from .Pmax import PmaxCls
			self._pmax = PmaxCls(self._core, self._cmd_group)
		return self._pmax

	@property
	def prStep(self):
		"""prStep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prStep'):
			from .PrStep import PrStepCls
			self._prStep = PrStepCls(self._core, self._cmd_group)
		return self._prStep

	@property
	def iptPower(self):
		"""iptPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iptPower'):
			from .IptPower import IptPowerCls
			self._iptPower = IptPowerCls(self._core, self._cmd_group)
		return self._iptPower

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindex'):
			from .Cindex import CindexCls
			self._cindex = CindexCls(self._core, self._cmd_group)
		return self._cindex

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
	def hsFlag(self):
		"""hsFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsFlag'):
			from .HsFlag import HsFlagCls
			self._hsFlag = HsFlagCls(self._core, self._cmd_group)
		return self._hsFlag

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
