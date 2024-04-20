from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 214 total commands, 23 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def pcid(self):
		"""pcid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcid'):
			from .Pcid import PcidCls
			self._pcid = PcidCls(self._core, self._cmd_group)
		return self._pcid

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import InfoCls
			self._info = InfoCls(self._core, self._cmd_group)
		return self._info

	@property
	def barred(self):
		"""barred commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_barred'):
			from .Barred import BarredCls
			self._barred = BarredCls(self._core, self._cmd_group)
		return self._barred

	@property
	def ulIndication(self):
		"""ulIndication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulIndication'):
			from .UlIndication import UlIndicationCls
			self._ulIndication = UlIndicationCls(self._core, self._cmd_group)
		return self._ulIndication

	@property
	def bbCombining(self):
		"""bbCombining commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbCombining'):
			from .BbCombining import BbCombiningCls
			self._bbCombining = BbCombiningCls(self._core, self._cmd_group)
		return self._bbCombining

	@property
	def mconfig(self):
		"""mconfig commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_mconfig'):
			from .Mconfig import MconfigCls
			self._mconfig = MconfigCls(self._core, self._cmd_group)
		return self._mconfig

	@property
	def rfSettings(self):
		"""rfSettings commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def tdd(self):
		"""tdd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import TddCls
			self._tdd = TddCls(self._core, self._cmd_group)
		return self._tdd

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
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def pusch(self):
		"""pusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def antenna(self):
		"""antenna commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	@property
	def mimo(self):
		"""mimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import MimoCls
			self._mimo = MimoCls(self._core, self._cmd_group)
		return self._mimo

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .UeScheduling import UeSchedulingCls
			self._ueScheduling = UeSchedulingCls(self._core, self._cmd_group)
		return self._ueScheduling

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .CqiReporting import CqiReportingCls
			self._cqiReporting = CqiReportingCls(self._core, self._cmd_group)
		return self._cqiReporting

	@property
	def harq(self):
		"""harq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import HarqCls
			self._harq = HarqCls(self._core, self._cmd_group)
		return self._harq

	@property
	def cdrx(self):
		"""cdrx commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdrx'):
			from .Cdrx import CdrxCls
			self._cdrx = CdrxCls(self._core, self._cmd_group)
		return self._cdrx

	@property
	def srs(self):
		"""srs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	@property
	def timeout(self):
		"""timeout commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_timeout'):
			from .Timeout import TimeoutCls
			self._timeout = TimeoutCls(self._core, self._cmd_group)
		return self._timeout

	@property
	def reSelection(self):
		"""reSelection commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_reSelection'):
			from .ReSelection import ReSelectionCls
			self._reSelection = ReSelectionCls(self._core, self._cmd_group)
		return self._reSelection

	@property
	def pcycle(self):
		"""pcycle commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcycle'):
			from .Pcycle import PcycleCls
			self._pcycle = PcycleCls(self._core, self._cmd_group)
		return self._pcycle

	@property
	def cmatrix(self):
		"""cmatrix commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmatrix'):
			from .Cmatrix import CmatrixCls
			self._cmatrix = CmatrixCls(self._core, self._cmd_group)
		return self._cmatrix

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
