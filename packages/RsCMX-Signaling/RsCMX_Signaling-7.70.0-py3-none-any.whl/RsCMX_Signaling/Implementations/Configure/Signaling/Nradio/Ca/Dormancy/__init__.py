from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DormancyCls:
	"""Dormancy commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dormancy", core, parent)

	@property
	def switch(self):
		"""switch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_switch'):
			from .Switch import SwitchCls
			self._switch = SwitchCls(self._core, self._cmd_group)
		return self._switch

	def clone(self) -> 'DormancyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DormancyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
