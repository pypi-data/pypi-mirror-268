from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QosFlowCls:
	"""QosFlow commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qosFlow", core, parent)

	def delete(self, ue_id: str, pdu_session_id: int, qos_flow_id: int) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow \n
		Snippet: driver.signaling.topology.fgs.ue.pdu.qosFlow.delete(ue_id = 'abc', pdu_session_id = 1, qos_flow_id = 1) \n
		Removes a QoS flow from a PDU session. \n
			:param ue_id: For future use. Enter any value.
			:param pdu_session_id: ID of the PDU session from which the QoS flow is removed.
			:param qos_flow_id: ID of the QoS flow to be removed (QFI) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String), ArgSingle('pdu_session_id', pdu_session_id, DataType.Integer), ArgSingle('qos_flow_id', qos_flow_id, DataType.Integer))
		self._core.io.write(f'DELete:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow {param}'.rstrip())
