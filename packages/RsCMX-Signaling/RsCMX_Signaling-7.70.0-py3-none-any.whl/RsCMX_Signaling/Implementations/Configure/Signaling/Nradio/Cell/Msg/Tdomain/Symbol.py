from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolCls:
	"""Symbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbol", core, parent)

	def set(self, cell_name: str, number_symbol: int, start_symbol: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MSG<id>:TDOMain:SYMBol \n
		Snippet: driver.configure.signaling.nradio.cell.msg.tdomain.symbol.set(cell_name = 'abc', number_symbol = 1, start_symbol = 1) \n
		Configures the allocated OFDM symbols for msg3. \n
			:param cell_name: No help available
			:param number_symbol: Number of allocated OFDM symbols.
			:param start_symbol: Index of the first allocated OFDM symbol.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('number_symbol', number_symbol, DataType.Integer), ArgSingle('start_symbol', start_symbol, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:MSG3:TDOMain:SYMBol {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Symbol: int: Number of allocated OFDM symbols.
			- Start_Symbol: int: Index of the first allocated OFDM symbol."""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Symbol'),
			ArgStruct.scalar_int('Start_Symbol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Symbol: int = None
			self.Start_Symbol: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MSG<id>:TDOMain:SYMBol \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.msg.tdomain.symbol.get(cell_name = 'abc') \n
		Configures the allocated OFDM symbols for msg3. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:MSG3:TDOMain:SYMBol? {param}', self.__class__.GetStruct())
