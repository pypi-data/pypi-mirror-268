from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NdBwpCls:
	"""NdBwp commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndBwp", core, parent)

	@property
	def waTime(self):
		"""waTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waTime'):
			from .WaTime import WaTimeCls
			self._waTime = WaTimeCls(self._core, self._cmd_group)
		return self._waTime

	@property
	def oaTime(self):
		"""oaTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oaTime'):
			from .OaTime import OaTimeCls
			self._oaTime = OaTimeCls(self._core, self._cmd_group)
		return self._oaTime

	def clone(self) -> 'NdBwpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NdBwpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
