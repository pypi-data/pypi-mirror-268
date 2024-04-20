from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefinedCls:
	"""UserDefined commands group definition. 36 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("userDefined", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def csScheduling(self):
		"""csScheduling commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csScheduling'):
			from .CsScheduling import CsSchedulingCls
			self._csScheduling = CsSchedulingCls(self._core, self._cmd_group)
		return self._csScheduling

	@property
	def uplink(self):
		"""uplink commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def sassignment(self):
		"""sassignment commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sassignment'):
			from .Sassignment import SassignmentCls
			self._sassignment = SassignmentCls(self._core, self._cmd_group)
		return self._sassignment

	def clone(self) -> 'UserDefinedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefinedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
