from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CssZeroCls:
	"""CssZero commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cssZero", core, parent)

	@property
	def crZero(self):
		"""crZero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crZero'):
			from .CrZero import CrZeroCls
			self._crZero = CrZeroCls(self._core, self._cmd_group)
		return self._crZero

	@property
	def ssZero(self):
		"""ssZero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssZero'):
			from .SsZero import SsZeroCls
			self._ssZero = SsZeroCls(self._core, self._cmd_group)
		return self._ssZero

	def clone(self) -> 'CssZeroCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CssZeroCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
