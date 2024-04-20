from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwpCls:
	"""Bwp commands group definition. 186 total commands, 19 Subgroups, 0 group commands
	Repeated Capability: BwParts, default value after init: BwParts.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwp", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bwParts_get', 'repcap_bwParts_set', repcap.BwParts.Nr1)

	def repcap_bwParts_set(self, bwParts: repcap.BwParts) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BwParts.Default
		Default value after init: BwParts.Nr1"""
		self._cmd_group.set_repcap_enum_value(bwParts)

	def repcap_bwParts_get(self) -> repcap.BwParts:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def smode(self):
		"""smode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smode'):
			from .Smode import SmodeCls
			self._smode = SmodeCls(self._core, self._cmd_group)
		return self._smode

	@property
	def target(self):
		"""target commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_target'):
			from .Target import TargetCls
			self._target = TargetCls(self._core, self._cmd_group)
		return self._target

	@property
	def downlink(self):
		"""downlink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def asMode(self):
		"""asMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asMode'):
			from .AsMode import AsModeCls
			self._asMode = AsModeCls(self._core, self._cmd_group)
		return self._asMode

	@property
	def sue(self):
		"""sue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sue'):
			from .Sue import SueCls
			self._sue = SueCls(self._core, self._cmd_group)
		return self._sue

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	@property
	def uplink(self):
		"""uplink commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
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
	def csi(self):
		"""csi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import CsiCls
			self._csi = CsiCls(self._core, self._cmd_group)
		return self._csi

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .UeScheduling import UeSchedulingCls
			self._ueScheduling = UeSchedulingCls(self._core, self._cmd_group)
		return self._ueScheduling

	@property
	def nssb(self):
		"""nssb commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_nssb'):
			from .Nssb import NssbCls
			self._nssb = NssbCls(self._core, self._cmd_group)
		return self._nssb

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
	def tadvance(self):
		"""tadvance commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tadvance'):
			from .Tadvance import TadvanceCls
			self._tadvance = TadvanceCls(self._core, self._cmd_group)
		return self._tadvance

	@property
	def dmrs(self):
		"""dmrs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Dmrs import DmrsCls
			self._dmrs = DmrsCls(self._core, self._cmd_group)
		return self._dmrs

	@property
	def srs(self):
		"""srs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	def clone(self) -> 'BwpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
