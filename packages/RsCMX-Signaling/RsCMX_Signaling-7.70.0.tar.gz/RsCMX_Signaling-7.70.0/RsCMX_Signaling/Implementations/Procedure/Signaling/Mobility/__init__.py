from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MobilityCls:
	"""Mobility commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mobility", core, parent)

	@property
	def handover(self):
		"""handover commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_handover'):
			from .Handover import HandoverCls
			self._handover = HandoverCls(self._core, self._cmd_group)
		return self._handover

	def set_redirection(self, target_cell: str) -> None:
		"""SCPI: PROCedure:SIGNaling:MOBility:REDirection \n
		Snippet: driver.procedure.signaling.mobility.set_redirection(target_cell = 'abc') \n
		Triggers a redirection from the current PCell to the <TargetCell>. \n
			:param target_cell: Name of the target cell of the redirection.
		"""
		param = Conversions.value_to_quoted_str(target_cell)
		self._core.io.write(f'PROCedure:SIGNaling:MOBility:REDirection {param}')

	def clone(self) -> 'MobilityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MobilityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
