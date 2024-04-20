from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Follow_Cqi: enums.FollowCqi: DISabled: No follow CQI. WB: Follow WB CQI. MSB: Follow maximum SB CQI. UEPSubband: Follow UE-preferred SB CQI. UEBSubband: Follow the best SB CQI.
			- Follow_Pmi: enums.FollowPmi: DISabled: No follow PMI. WB: Follow WB PMI. WBEXplicit: Follow WB PMI and PMI sent to the UE via DCI. SB: Follow SB PMI.
			- Follow_Ri: enums.FollowRi: DISabled: No follow RI. ENABled: New RI applied after the current retransmission cycle. RETX: New RI applied immediately, also for retransmissions."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Follow_Cqi', enums.FollowCqi),
			ArgStruct.scalar_enum('Follow_Pmi', enums.FollowPmi),
			ArgStruct.scalar_enum('Follow_Ri', enums.FollowRi)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Follow_Cqi: enums.FollowCqi = None
			self.Follow_Pmi: enums.FollowPmi = None
			self.Follow_Ri: enums.FollowRi = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: SENSe:SIGNaling:LTE:CELL:UESCheduling:DYNamic:DL:TYPE \n
		Snippet: value: GetStruct = driver.sense.signaling.lte.cell.ueScheduling.dynamic.downlink.typePy.get(cell_name = 'abc') \n
		Queries which follow modes are active for the DL. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'SENSe:SIGNaling:LTE:CELL:UESCheduling:DYNamic:DL:TYPE? {param}', self.__class__.GetStruct())
