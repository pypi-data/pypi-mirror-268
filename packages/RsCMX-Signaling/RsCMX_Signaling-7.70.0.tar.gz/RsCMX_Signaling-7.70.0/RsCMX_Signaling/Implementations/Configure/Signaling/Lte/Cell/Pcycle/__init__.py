from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcycleCls:
	"""Pcycle commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcycle", core, parent)

	@property
	def pcycle(self):
		"""pcycle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcycle'):
			from .Pcycle import PcycleCls
			self._pcycle = PcycleCls(self._core, self._cmd_group)
		return self._pcycle

	@property
	def pfOffset(self):
		"""pfOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfOffset'):
			from .PfOffset import PfOffsetCls
			self._pfOffset = PfOffsetCls(self._core, self._cmd_group)
		return self._pfOffset

	def clone(self) -> 'PcycleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PcycleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
