from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QosFlowCls:
	"""QosFlow commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qosFlow", core, parent)

	def get(self, ue_id: str, pdu_session_id: int) -> List[int]:
		"""SCPI: CATalog:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow \n
		Snippet: value: List[int] = driver.catalog.signaling.topology.fgs.ue.pdu.qosFlow.get(ue_id = 'abc', pdu_session_id = 1) \n
		Queries a list of all QoS flows of a PDU session. \n
			:param ue_id: For future use. Enter any value.
			:param pdu_session_id: ID of the PDU session for which the QoS flows are queried.
			:return: qos_flow_id: Comma-separated list of QoS flow IDs."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String), ArgSingle('pdu_session_id', pdu_session_id, DataType.Integer))
		response = self._core.io.query_bin_or_ascii_int_list(f'CATalog:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow? {param}'.rstrip())
		return response
