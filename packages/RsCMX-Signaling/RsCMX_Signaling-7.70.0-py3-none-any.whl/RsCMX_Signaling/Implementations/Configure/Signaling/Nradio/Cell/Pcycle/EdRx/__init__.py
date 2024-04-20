from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdRxCls:
	"""EdRx commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edRx", core, parent)

	@property
	def aidle(self):
		"""aidle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aidle'):
			from .Aidle import AidleCls
			self._aidle = AidleCls(self._core, self._cmd_group)
		return self._aidle

	@property
	def ainactive(self):
		"""ainactive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ainactive'):
			from .Ainactive import AinactiveCls
			self._ainactive = AinactiveCls(self._core, self._cmd_group)
		return self._ainactive

	def clone(self) -> 'EdRxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EdRxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
