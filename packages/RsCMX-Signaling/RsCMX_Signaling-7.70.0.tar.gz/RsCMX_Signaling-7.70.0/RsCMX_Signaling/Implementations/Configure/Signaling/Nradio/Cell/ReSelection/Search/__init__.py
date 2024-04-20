from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchCls:
	"""Search commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("search", core, parent)

	@property
	def ninp(self):
		"""ninp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ninp'):
			from .Ninp import NinpCls
			self._ninp = NinpCls(self._core, self._cmd_group)
		return self._ninp

	@property
	def ninq(self):
		"""ninq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ninq'):
			from .Ninq import NinqCls
			self._ninq = NinqCls(self._core, self._cmd_group)
		return self._ninq

	@property
	def intp(self):
		"""intp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_intp'):
			from .Intp import IntpCls
			self._intp = IntpCls(self._core, self._cmd_group)
		return self._intp

	@property
	def intq(self):
		"""intq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_intq'):
			from .Intq import IntqCls
			self._intq = IntqCls(self._core, self._cmd_group)
		return self._intq

	def clone(self) -> 'SearchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SearchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
