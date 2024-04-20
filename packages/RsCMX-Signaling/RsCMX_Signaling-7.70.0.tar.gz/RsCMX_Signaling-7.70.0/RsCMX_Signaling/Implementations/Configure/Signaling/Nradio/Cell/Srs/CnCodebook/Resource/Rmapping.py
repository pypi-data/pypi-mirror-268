from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmappingCls:
	"""Rmapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmapping", core, parent)

	def set(self, cell_name: str, resource_no: int, start_position: int, no_symbols: enums.NoSymbolsN = None, rep_factor: enums.NoSymbolsN = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource:RMAPping \n
		Snippet: driver.configure.signaling.nradio.cell.srs.cnCodebook.resource.rmapping.set(cell_name = 'abc', resource_no = 1, start_position = 1, no_symbols = enums.NoSymbolsN.N1, rep_factor = enums.NoSymbolsN.N1) \n
		Configures the resource mapping for SRS transmissions, for SRS resource <ResourceNo> for periodic SRS, for the initial
		BWP. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:param start_position: No help available
			:param no_symbols: No help available
			:param rep_factor: Repetition factor
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer), ArgSingle('start_position', start_position, DataType.Integer), ArgSingle('no_symbols', no_symbols, DataType.Enum, enums.NoSymbolsN, is_optional=True), ArgSingle('rep_factor', rep_factor, DataType.Enum, enums.NoSymbolsN, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource:RMAPping {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Start_Position: int: No parameter help available
			- No_Symbols: enums.NoSymbolsN: No parameter help available
			- Rep_Factor: enums.NoSymbolsN: Repetition factor"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Position'),
			ArgStruct.scalar_enum('No_Symbols', enums.NoSymbolsN),
			ArgStruct.scalar_enum('Rep_Factor', enums.NoSymbolsN)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Position: int = None
			self.No_Symbols: enums.NoSymbolsN = None
			self.Rep_Factor: enums.NoSymbolsN = None

	def get(self, cell_name: str, resource_no: int) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource:RMAPping \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.srs.cnCodebook.resource.rmapping.get(cell_name = 'abc', resource_no = 1) \n
		Configures the resource mapping for SRS transmissions, for SRS resource <ResourceNo> for periodic SRS, for the initial
		BWP. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource:RMAPping? {param}'.rstrip(), self.__class__.GetStruct())
