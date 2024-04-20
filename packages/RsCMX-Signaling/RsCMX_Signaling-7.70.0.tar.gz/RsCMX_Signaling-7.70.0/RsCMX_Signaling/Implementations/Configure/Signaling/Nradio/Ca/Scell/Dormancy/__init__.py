from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DormancyCls:
	"""Dormancy commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dormancy", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def dbwp(self):
		"""dbwp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbwp'):
			from .Dbwp import DbwpCls
			self._dbwp = DbwpCls(self._core, self._cmd_group)
		return self._dbwp

	@property
	def ndBwp(self):
		"""ndBwp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ndBwp'):
			from .NdBwp import NdBwpCls
			self._ndBwp = NdBwpCls(self._core, self._cmd_group)
		return self._ndBwp

	def clone(self) -> 'DormancyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DormancyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
