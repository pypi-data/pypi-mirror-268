from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Type_Dl: enums.TypeDlUl: For downlink
			- Type_Ul: enums.TypeDlUl: For uplink"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Type_Dl', enums.TypeDlUl),
			ArgStruct.scalar_enum('Type_Ul', enums.TypeDlUl)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Type_Dl: enums.TypeDlUl = None
			self.Type_Ul: enums.TypeDlUl = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:UESCheduling:TYPE \n
		Snippet: value: GetStruct = driver.sense.signaling.nradio.cell.ueScheduling.typePy.get(cell_name = 'abc') \n
		Queries whether the downlink and uplink scheduling settings correspond to an RMC defined by 3GPP (RMC) or not (UDEFined) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'SENSe:SIGNaling:NRADio:CELL:UESCheduling:TYPE? {param}', self.__class__.GetStruct())
