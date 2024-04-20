from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 532 total commands, 38 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def mconfig(self):
		"""mconfig commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_mconfig'):
			from .Mconfig import MconfigCls
			self._mconfig = MconfigCls(self._core, self._cmd_group)
		return self._mconfig

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import InfoCls
			self._info = InfoCls(self._core, self._cmd_group)
		return self._info

	@property
	def pcid(self):
		"""pcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcid'):
			from .Pcid import PcidCls
			self._pcid = PcidCls(self._core, self._cmd_group)
		return self._pcid

	@property
	def barred(self):
		"""barred commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_barred'):
			from .Barred import BarredCls
			self._barred = BarredCls(self._core, self._cmd_group)
		return self._barred

	@property
	def ueType(self):
		"""ueType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ueType'):
			from .UeType import UeTypeCls
			self._ueType = UeTypeCls(self._core, self._cmd_group)
		return self._ueType

	@property
	def bbCombining(self):
		"""bbCombining commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbCombining'):
			from .BbCombining import BbCombiningCls
			self._bbCombining = BbCombiningCls(self._core, self._cmd_group)
		return self._bbCombining

	@property
	def rfSettings(self):
		"""rfSettings commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def bwp(self):
		"""bwp commands group. 19 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwp'):
			from .Bwp import BwpCls
			self._bwp = BwpCls(self._core, self._cmd_group)
		return self._bwp

	@property
	def ibwp(self):
		"""ibwp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ibwp'):
			from .Ibwp import IbwpCls
			self._ibwp = IbwpCls(self._core, self._cmd_group)
		return self._ibwp

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def pucch(self):
		"""pucch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def msg(self):
		"""msg commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_msg'):
			from .Msg import MsgCls
			self._msg = MsgCls(self._core, self._cmd_group)
		return self._msg

	@property
	def tdd(self):
		"""tdd commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

	@property
	def alayout(self):
		"""alayout commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_alayout'):
			from .Alayout import AlayoutCls
			self._alayout = AlayoutCls(self._core, self._cmd_group)
		return self._alayout

	@property
	def csi(self):
		"""csi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import CsiCls
			self._csi = CsiCls(self._core, self._cmd_group)
		return self._csi

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .UeScheduling import UeSchedulingCls
			self._ueScheduling = UeSchedulingCls(self._core, self._cmd_group)
		return self._ueScheduling

	@property
	def cssZero(self):
		"""cssZero commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cssZero'):
			from .CssZero import CssZeroCls
			self._cssZero = CssZeroCls(self._core, self._cmd_group)
		return self._cssZero

	@property
	def nssb(self):
		"""nssb commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_nssb'):
			from .Nssb import NssbCls
			self._nssb = NssbCls(self._core, self._cmd_group)
		return self._nssb

	@property
	def ssb(self):
		"""ssb commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssb'):
			from .Ssb import SsbCls
			self._ssb = SsbCls(self._core, self._cmd_group)
		return self._ssb

	@property
	def harq(self):
		"""harq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import HarqCls
			self._harq = HarqCls(self._core, self._cmd_group)
		return self._harq

	@property
	def bler(self):
		"""bler commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bler'):
			from .Bler import BlerCls
			self._bler = BlerCls(self._core, self._cmd_group)
		return self._bler

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .CqiReporting import CqiReportingCls
			self._cqiReporting = CqiReportingCls(self._core, self._cmd_group)
		return self._cqiReporting

	@property
	def cdrx(self):
		"""cdrx commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdrx'):
			from .Cdrx import CdrxCls
			self._cdrx = CdrxCls(self._core, self._cmd_group)
		return self._cdrx

	@property
	def cmatrix(self):
		"""cmatrix commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Cmatrix import CmatrixCls
			self._cmatrix = CmatrixCls(self._core, self._cmd_group)
		return self._cmatrix

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_timeout'):
			from .Timeout import TimeoutCls
			self._timeout = TimeoutCls(self._core, self._cmd_group)
		return self._timeout

	@property
	def timing(self):
		"""timing commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import TimingCls
			self._timing = TimingCls(self._core, self._cmd_group)
		return self._timing

	@property
	def tadvance(self):
		"""tadvance commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tadvance'):
			from .Tadvance import TadvanceCls
			self._tadvance = TadvanceCls(self._core, self._cmd_group)
		return self._tadvance

	@property
	def reSelection(self):
		"""reSelection commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_reSelection'):
			from .ReSelection import ReSelectionCls
			self._reSelection = ReSelectionCls(self._core, self._cmd_group)
		return self._reSelection

	@property
	def pcycle(self):
		"""pcycle commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcycle'):
			from .Pcycle import PcycleCls
			self._pcycle = PcycleCls(self._core, self._cmd_group)
		return self._pcycle

	@property
	def dmrs(self):
		"""dmrs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import DmrsCls
			self._dmrs = DmrsCls(self._core, self._cmd_group)
		return self._dmrs

	@property
	def srs(self):
		"""srs commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	@property
	def beam(self):
		"""beam commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_beam'):
			from .Beam import BeamCls
			self._beam = BeamCls(self._core, self._cmd_group)
		return self._beam

	@property
	def asn(self):
		"""asn commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_asn'):
			from .Asn import AsnCls
			self._asn = AsnCls(self._core, self._cmd_group)
		return self._asn

	@property
	def beams(self):
		"""beams commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_beams'):
			from .Beams import BeamsCls
			self._beams = BeamsCls(self._core, self._cmd_group)
		return self._beams

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
