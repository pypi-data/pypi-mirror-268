from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrcCls:
	"""Rrc commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrc", core, parent)

	@property
	def inactive(self):
		"""inactive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inactive'):
			from .Inactive import InactiveCls
			self._inactive = InactiveCls(self._core, self._cmd_group)
		return self._inactive

	@property
	def resume(self):
		"""resume commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resume'):
			from .Resume import ResumeCls
			self._resume = ResumeCls(self._core, self._cmd_group)
		return self._resume

	def set(self, ue_id: str, action: enums.Action) -> None:
		"""SCPI: PROCedure:SIGNaling:UE:RRC \n
		Snippet: driver.procedure.signaling.ue.rrc.set(ue_id = 'abc', action = enums.Action.CONNect) \n
		Establishes or releases an RRC connection. \n
			:param ue_id: No help available
			:param action: DISConnect: release connection to idle CONNect: establish RRC connection
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String), ArgSingle('action', action, DataType.Enum, enums.Action))
		self._core.io.write(f'PROCedure:SIGNaling:UE:RRC {param}'.rstrip())

	def clone(self) -> 'RrcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RrcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
