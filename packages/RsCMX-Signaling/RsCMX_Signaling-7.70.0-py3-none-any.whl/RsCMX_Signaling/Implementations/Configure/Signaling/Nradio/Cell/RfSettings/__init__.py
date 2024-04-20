from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 29 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def frange(self):
		"""frange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frange'):
			from .Frange import FrangeCls
			self._frange = FrangeCls(self._core, self._cmd_group)
		return self._frange

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	@property
	def rbMax(self):
		"""rbMax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbMax'):
			from .RbMax import RbMaxCls
			self._rbMax = RbMaxCls(self._core, self._cmd_group)
		return self._rbMax

	@property
	def dmode(self):
		"""dmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmode'):
			from .Dmode import DmodeCls
			self._dmode = DmodeCls(self._core, self._cmd_group)
		return self._dmode

	@property
	def fbIndicator(self):
		"""fbIndicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fbIndicator'):
			from .FbIndicator import FbIndicatorCls
			self._fbIndicator = FbIndicatorCls(self._core, self._cmd_group)
		return self._fbIndicator

	@property
	def downlink(self):
		"""downlink commands group. 5 Sub-classes, 0 commands."""
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
	def apoint(self):
		"""apoint commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apoint'):
			from .Apoint import ApointCls
			self._apoint = ApointCls(self._core, self._cmd_group)
		return self._apoint

	@property
	def asEmission(self):
		"""asEmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asEmission'):
			from .AsEmission import AsEmissionCls
			self._asEmission = AsEmissionCls(self._core, self._cmd_group)
		return self._asEmission

	@property
	def combined(self):
		"""combined commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_combined'):
			from .Combined import CombinedCls
			self._combined = CombinedCls(self._core, self._cmd_group)
		return self._combined

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
