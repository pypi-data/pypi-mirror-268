from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsgCls:
	"""Msg commands group definition. 3 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msg", core, parent)

	@property
	def tdomain(self):
		"""tdomain commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdomain'):
			from .Tdomain import TdomainCls
			self._tdomain = TdomainCls(self._core, self._cmd_group)
		return self._tdomain

	def clone(self) -> 'MsgCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MsgCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
