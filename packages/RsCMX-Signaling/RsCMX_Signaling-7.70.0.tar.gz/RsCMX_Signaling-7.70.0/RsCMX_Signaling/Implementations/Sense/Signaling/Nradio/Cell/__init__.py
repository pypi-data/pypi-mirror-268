from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 25 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def bbgIndex(self):
		"""bbgIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbgIndex'):
			from .BbgIndex import BbgIndexCls
			self._bbgIndex = BbgIndexCls(self._core, self._cmd_group)
		return self._bbgIndex

	@property
	def rfSettings(self):
		"""rfSettings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def bwp(self):
		"""bwp commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwp'):
			from .Bwp import BwpCls
			self._bwp = BwpCls(self._core, self._cmd_group)
		return self._bwp

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def alayout(self):
		"""alayout commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_alayout'):
			from .Alayout import AlayoutCls
			self._alayout = AlayoutCls(self._core, self._cmd_group)
		return self._alayout

	@property
	def ueScheduling(self):
		"""ueScheduling commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueScheduling'):
			from .UeScheduling import UeSchedulingCls
			self._ueScheduling = UeSchedulingCls(self._core, self._cmd_group)
		return self._ueScheduling

	@property
	def ssb(self):
		"""ssb commands group. 1 Sub-classes, 0 commands."""
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
	def cqiReporting(self):
		"""cqiReporting commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .CqiReporting import CqiReportingCls
			self._cqiReporting = CqiReportingCls(self._core, self._cmd_group)
		return self._cqiReporting

	@property
	def beams(self):
		"""beams commands group. 1 Sub-classes, 0 commands."""
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
