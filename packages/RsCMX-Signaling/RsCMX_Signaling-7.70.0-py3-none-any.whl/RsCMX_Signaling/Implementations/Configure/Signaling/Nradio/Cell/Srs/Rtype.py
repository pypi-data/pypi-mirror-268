from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RtypeCls:
	"""Rtype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtype", core, parent)

	def set(self, cell_name: str, td_type: enums.TdType, period: int = None, offset: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:RTYPe \n
		Snippet: driver.configure.signaling.nradio.cell.srs.rtype.set(cell_name = 'abc', td_type = enums.TdType.APERiodic, period = 1, offset = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param td_type: No help available
			:param period: No help available
			:param offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('td_type', td_type, DataType.Enum, enums.TdType), ArgSingle('period', period, DataType.Integer, None, is_optional=True), ArgSingle('offset', offset, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:RTYPe {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Td_Type: enums.TdType: No parameter help available
			- Period: int: No parameter help available
			- Offset: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Td_Type', enums.TdType),
			ArgStruct.scalar_int('Period'),
			ArgStruct.scalar_int('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Td_Type: enums.TdType = None
			self.Period: int = None
			self.Offset: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:RTYPe \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.srs.rtype.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:SRS:RTYPe? {param}', self.__class__.GetStruct())
