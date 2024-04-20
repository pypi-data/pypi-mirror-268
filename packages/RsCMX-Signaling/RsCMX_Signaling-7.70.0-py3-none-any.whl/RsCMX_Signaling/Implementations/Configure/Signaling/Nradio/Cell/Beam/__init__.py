from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BeamCls:
	"""Beam commands group definition. 7 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("beam", core, parent)

	@property
	def following(self):
		"""following commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_following'):
			from .Following import FollowingCls
			self._following = FollowingCls(self._core, self._cmd_group)
		return self._following

	@property
	def frecovery(self):
		"""frecovery commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frecovery'):
			from .Frecovery import FrecoveryCls
			self._frecovery = FrecoveryCls(self._core, self._cmd_group)
		return self._frecovery

	def clone(self) -> 'BeamCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BeamCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
