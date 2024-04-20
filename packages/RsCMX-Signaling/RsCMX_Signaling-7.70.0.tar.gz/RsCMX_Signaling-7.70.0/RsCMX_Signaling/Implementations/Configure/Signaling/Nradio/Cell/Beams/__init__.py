from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BeamsCls:
	"""Beams commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("beams", core, parent)

	@property
	def nbBeams(self):
		"""nbBeams commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbBeams'):
			from .NbBeams import NbBeamsCls
			self._nbBeams = NbBeamsCls(self._core, self._cmd_group)
		return self._nbBeams

	@property
	def beamConfig(self):
		"""beamConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_beamConfig'):
			from .BeamConfig import BeamConfigCls
			self._beamConfig = BeamConfigCls(self._core, self._cmd_group)
		return self._beamConfig

	@property
	def ap3Trigger(self):
		"""ap3Trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ap3Trigger'):
			from .Ap3Trigger import Ap3TriggerCls
			self._ap3Trigger = Ap3TriggerCls(self._core, self._cmd_group)
		return self._ap3Trigger

	@property
	def mtrigger(self):
		"""mtrigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtrigger'):
			from .Mtrigger import MtriggerCls
			self._mtrigger = MtriggerCls(self._core, self._cmd_group)
		return self._mtrigger

	def clone(self) -> 'BeamsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BeamsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
