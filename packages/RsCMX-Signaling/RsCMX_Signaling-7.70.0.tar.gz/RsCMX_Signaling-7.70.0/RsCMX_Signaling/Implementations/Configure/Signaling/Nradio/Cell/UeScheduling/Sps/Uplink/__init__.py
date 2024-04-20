from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def periodicity(self):
		"""periodicity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_periodicity'):
			from .Periodicity import PeriodicityCls
			self._periodicity = PeriodicityCls(self._core, self._cmd_group)
		return self._periodicity

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import AlevelCls
			self._alevel = AlevelCls(self._core, self._cmd_group)
		return self._alevel

	@property
	def ssid(self):
		"""ssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssid'):
			from .Ssid import SsidCls
			self._ssid = SsidCls(self._core, self._cmd_group)
		return self._ssid

	@property
	def raType(self):
		"""raType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_raType'):
			from .RaType import RaTypeCls
			self._raType = RaTypeCls(self._core, self._cmd_group)
		return self._raType

	@property
	def rbgSize(self):
		"""rbgSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbgSize'):
			from .RbgSize import RbgSizeCls
			self._rbgSize = RbgSizeCls(self._core, self._cmd_group)
		return self._rbgSize

	@property
	def nohp(self):
		"""nohp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nohp'):
			from .Nohp import NohpCls
			self._nohp = NohpCls(self._core, self._cmd_group)
		return self._nohp

	@property
	def tpEnable(self):
		"""tpEnable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpEnable'):
			from .TpEnable import TpEnableCls
			self._tpEnable = TpEnableCls(self._core, self._cmd_group)
		return self._tpEnable

	@property
	def cgTimer(self):
		"""cgTimer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cgTimer'):
			from .CgTimer import CgTimerCls
			self._cgTimer = CgTimerCls(self._core, self._cmd_group)
		return self._cgTimer

	@property
	def rrVersion(self):
		"""rrVersion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrVersion'):
			from .RrVersion import RrVersionCls
			self._rrVersion = RrVersionCls(self._core, self._cmd_group)
		return self._rrVersion

	@property
	def dmrsPosition(self):
		"""dmrsPosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmrsPosition'):
			from .DmrsPosition import DmrsPositionCls
			self._dmrsPosition = DmrsPositionCls(self._core, self._cmd_group)
		return self._dmrsPosition

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
