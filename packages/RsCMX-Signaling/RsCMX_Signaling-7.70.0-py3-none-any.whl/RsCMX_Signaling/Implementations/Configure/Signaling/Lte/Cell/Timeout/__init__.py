from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeoutCls:
	"""Timeout commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timeout", core, parent)

	@property
	def t(self):
		"""t commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_t'):
			from .T import TCls
			self._t = TCls(self._core, self._cmd_group)
		return self._t

	@property
	def n(self):
		"""n commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n'):
			from .N import NCls
			self._n = NCls(self._core, self._cmd_group)
		return self._n

	def clone(self) -> 'TimeoutCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimeoutCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
