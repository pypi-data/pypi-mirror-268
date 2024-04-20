from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SdrxCls:
	"""Sdrx commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdrx", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def cycle(self):
		"""cycle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycle'):
			from .Cycle import CycleCls
			self._cycle = CycleCls(self._core, self._cmd_group)
		return self._cycle

	@property
	def scTimer(self):
		"""scTimer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scTimer'):
			from .ScTimer import ScTimerCls
			self._scTimer = ScTimerCls(self._core, self._cmd_group)
		return self._scTimer

	def clone(self) -> 'SdrxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SdrxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
