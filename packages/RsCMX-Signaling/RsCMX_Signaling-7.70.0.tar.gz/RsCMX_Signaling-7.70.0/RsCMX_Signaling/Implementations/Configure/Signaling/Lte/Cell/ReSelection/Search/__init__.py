from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchCls:
	"""Search commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("search", core, parent)

	@property
	def nintrasearch(self):
		"""nintrasearch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nintrasearch'):
			from .Nintrasearch import NintrasearchCls
			self._nintrasearch = NintrasearchCls(self._core, self._cmd_group)
		return self._nintrasearch

	@property
	def intrasearch(self):
		"""intrasearch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_intrasearch'):
			from .Intrasearch import IntrasearchCls
			self._intrasearch = IntrasearchCls(self._core, self._cmd_group)
		return self._intrasearch

	def clone(self) -> 'SearchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SearchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
