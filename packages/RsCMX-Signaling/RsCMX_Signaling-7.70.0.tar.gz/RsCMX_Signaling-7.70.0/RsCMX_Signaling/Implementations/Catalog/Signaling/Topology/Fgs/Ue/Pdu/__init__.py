from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PduCls:
	"""Pdu commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdu", core, parent)

	@property
	def qosFlow(self):
		"""qosFlow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qosFlow'):
			from .QosFlow import QosFlowCls
			self._qosFlow = QosFlowCls(self._core, self._cmd_group)
		return self._qosFlow

	def get(self, ue_id: str = None) -> List[int]:
		"""SCPI: CATalog:SIGNaling:TOPology:FGS:UE:PDU \n
		Snippet: value: List[int] = driver.catalog.signaling.topology.fgs.ue.pdu.get(ue_id = 'abc') \n
		Queries a list of all established PDU sessions. \n
			:param ue_id: For future use. Enter any value.
			:return: pdu_session_id: Comma-separated list of PDU session IDs."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True))
		response = self._core.io.query_bin_or_ascii_int_list(f'CATalog:SIGNaling:TOPology:FGS:UE:PDU? {param}'.rstrip())
		return response

	def clone(self) -> 'PduCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PduCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
