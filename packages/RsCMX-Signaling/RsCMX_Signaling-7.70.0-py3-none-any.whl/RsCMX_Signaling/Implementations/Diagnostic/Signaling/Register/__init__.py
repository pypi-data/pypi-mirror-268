from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RegisterCls:
	"""Register commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("register", core, parent)

	@property
	def existing(self):
		"""existing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_existing'):
			from .Existing import ExistingCls
			self._existing = ExistingCls(self._core, self._cmd_group)
		return self._existing

	def clone(self) -> 'RegisterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RegisterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
