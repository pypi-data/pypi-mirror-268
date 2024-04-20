from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FoSymbolCls:
	"""FoSymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foSymbol", core, parent)

	def set(self, cell_name: str, symbol: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:RESource:FOSYmbol \n
		Snippet: driver.configure.signaling.nradio.cell.cqiReporting.resource.foSymbol.set(cell_name = 'abc', symbol = 1) \n
		Configures the first OFDM symbol in the RB used for CSI-RS. \n
			:param cell_name: No help available
			:param symbol: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('symbol', symbol, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:RESource:FOSYmbol {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:RESource:FOSYmbol \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.cqiReporting.resource.foSymbol.get(cell_name = 'abc') \n
		Configures the first OFDM symbol in the RB used for CSI-RS. \n
			:param cell_name: No help available
			:return: symbol: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:RESource:FOSYmbol? {param}')
		return Conversions.str_to_int(response)
