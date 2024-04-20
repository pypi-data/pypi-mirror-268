from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpsCls:
	"""Sps commands group definition. 13 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sps", core, parent)

	@property
	def sassignment(self):
		"""sassignment commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sassignment'):
			from .Sassignment import SassignmentCls
			self._sassignment = SassignmentCls(self._core, self._cmd_group)
		return self._sassignment

	def clone(self) -> 'SpsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
