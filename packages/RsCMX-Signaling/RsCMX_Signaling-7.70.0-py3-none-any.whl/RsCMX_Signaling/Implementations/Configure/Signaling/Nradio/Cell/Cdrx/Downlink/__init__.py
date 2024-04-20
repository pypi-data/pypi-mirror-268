from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def hrTimer(self):
		"""hrTimer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hrTimer'):
			from .HrTimer import HrTimerCls
			self._hrTimer = HrTimerCls(self._core, self._cmd_group)
		return self._hrTimer

	@property
	def rtimer(self):
		"""rtimer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtimer'):
			from .Rtimer import RtimerCls
			self._rtimer = RtimerCls(self._core, self._cmd_group)
		return self._rtimer

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
