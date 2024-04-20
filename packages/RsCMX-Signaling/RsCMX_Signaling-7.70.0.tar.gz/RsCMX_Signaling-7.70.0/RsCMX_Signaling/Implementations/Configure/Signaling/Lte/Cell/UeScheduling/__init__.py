from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeSchedulingCls:
	"""UeScheduling commands group definition. 86 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueScheduling", core, parent)

	@property
	def smode(self):
		"""smode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smode'):
			from .Smode import SmodeCls
			self._smode = SmodeCls(self._core, self._cmd_group)
		return self._smode

	@property
	def rmc(self):
		"""rmc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmc'):
			from .Rmc import RmcCls
			self._rmc = RmcCls(self._core, self._cmd_group)
		return self._rmc

	@property
	def cmMapping(self):
		"""cmMapping commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmMapping'):
			from .CmMapping import CmMappingCls
			self._cmMapping = CmMappingCls(self._core, self._cmd_group)
		return self._cmMapping

	@property
	def sps(self):
		"""sps commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sps'):
			from .Sps import SpsCls
			self._sps = SpsCls(self._core, self._cmd_group)
		return self._sps

	@property
	def userDefined(self):
		"""userDefined commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def laa(self):
		"""laa commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_laa'):
			from .Laa import LaaCls
			self._laa = LaaCls(self._core, self._cmd_group)
		return self._laa

	def clone(self) -> 'UeSchedulingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeSchedulingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
