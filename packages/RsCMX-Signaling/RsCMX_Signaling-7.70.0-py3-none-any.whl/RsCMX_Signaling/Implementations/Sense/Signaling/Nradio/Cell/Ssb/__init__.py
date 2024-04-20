from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsbCls:
	"""Ssb commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssb", core, parent)

	@property
	def beam(self):
		"""beam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_beam'):
			from .Beam import BeamCls
			self._beam = BeamCls(self._core, self._cmd_group)
		return self._beam

	def clone(self) -> 'SsbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SsbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
