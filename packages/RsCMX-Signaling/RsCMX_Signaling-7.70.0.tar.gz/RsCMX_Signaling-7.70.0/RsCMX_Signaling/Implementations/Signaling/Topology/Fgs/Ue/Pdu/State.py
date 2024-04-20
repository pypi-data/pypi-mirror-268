from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Pdu_Session_Id_Result: List[int]: No parameter help available
			- Pdu_State: List[enums.PduState]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Pdu_Session_Id_Result', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Pdu_State', DataType.EnumList, enums.PduState, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pdu_Session_Id_Result: List[int] = None
			self.Pdu_State: List[enums.PduState] = None

	def fetch(self, ue_id: str = None, pdu_session_id: int = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:TOPology:FGS:UE:PDU:STATe \n
		Snippet: value: FetchStruct = driver.signaling.topology.fgs.ue.pdu.state.fetch(ue_id = 'abc', pdu_session_id = 1) \n
		No command help available \n
			:param ue_id: No help available
			:param pdu_session_id: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True), ArgSingle('pdu_session_id', pdu_session_id, DataType.Integer, None, is_optional=True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:TOPology:FGS:UE:PDU:STATe? {param}'.rstrip(), self.__class__.FetchStruct())
