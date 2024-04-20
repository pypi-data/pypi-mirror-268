from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Follow_Cqi: enums.FollowType: No parameter help available
			- Follow_Pmi: enums.FollowType: No parameter help available
			- Follow_Ri: enums.FollowType: No parameter help available
			- Follow_Bo: enums.FollowType: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Follow_Cqi', enums.FollowType),
			ArgStruct.scalar_enum('Follow_Pmi', enums.FollowType),
			ArgStruct.scalar_enum('Follow_Ri', enums.FollowType),
			ArgStruct.scalar_enum('Follow_Bo', enums.FollowType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Follow_Cqi: enums.FollowType = None
			self.Follow_Pmi: enums.FollowType = None
			self.Follow_Ri: enums.FollowType = None
			self.Follow_Bo: enums.FollowType = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:UESCheduling:DYNamic:TYPE \n
		Snippet: value: GetStruct = driver.sense.signaling.nradio.cell.ueScheduling.dynamic.typePy.get(cell_name = 'abc') \n
		Queries which follow modes are active, for the initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'SENSe:SIGNaling:NRADio:CELL:UESCheduling:DYNamic:TYPE? {param}', self.__class__.GetStruct())
