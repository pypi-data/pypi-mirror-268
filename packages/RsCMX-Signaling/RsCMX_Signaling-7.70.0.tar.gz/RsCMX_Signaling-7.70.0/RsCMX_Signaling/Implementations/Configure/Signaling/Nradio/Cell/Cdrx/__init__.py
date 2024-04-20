from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdrxCls:
	"""Cdrx commands group definition. 19 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdrx", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def aaScheduler(self):
		"""aaScheduler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aaScheduler'):
			from .AaScheduler import AaSchedulerCls
			self._aaScheduler = AaSchedulerCls(self._core, self._cmd_group)
		return self._aaScheduler

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def odTimer(self):
		"""odTimer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_odTimer'):
			from .OdTimer import OdTimerCls
			self._odTimer = OdTimerCls(self._core, self._cmd_group)
		return self._odTimer

	@property
	def itimer(self):
		"""itimer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_itimer'):
			from .Itimer import ItimerCls
			self._itimer = ItimerCls(self._core, self._cmd_group)
		return self._itimer

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Soffset import SoffsetCls
			self._soffset = SoffsetCls(self._core, self._cmd_group)
		return self._soffset

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def ldrx(self):
		"""ldrx commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ldrx'):
			from .Ldrx import LdrxCls
			self._ldrx = LdrxCls(self._core, self._cmd_group)
		return self._ldrx

	@property
	def wus(self):
		"""wus commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_wus'):
			from .Wus import WusCls
			self._wus = WusCls(self._core, self._cmd_group)
		return self._wus

	@property
	def sdrx(self):
		"""sdrx commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdrx'):
			from .Sdrx import SdrxCls
			self._sdrx = SdrxCls(self._core, self._cmd_group)
		return self._sdrx

	def clone(self) -> 'CdrxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CdrxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
