from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OslSubframeCls:
	"""OslSubframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oslSubframe", core, parent)

	def set(self, cell_name: str, ofdm_symbols: enums.OfdmSymbols) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:OSLSubframe \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.oslSubframe.set(cell_name = 'abc', ofdm_symbols = enums.OfdmSymbols.ALL) \n
		Selects the number of allocated OFDM symbols at the beginning of the last subframe of a fixed burst. \n
			:param cell_name: No help available
			:param ofdm_symbols: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ofdm_symbols', ofdm_symbols, DataType.Enum, enums.OfdmSymbols))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:OSLSubframe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.OfdmSymbols:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:OSLSubframe \n
		Snippet: value: enums.OfdmSymbols = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.oslSubframe.get(cell_name = 'abc') \n
		Selects the number of allocated OFDM symbols at the beginning of the last subframe of a fixed burst. \n
			:param cell_name: No help available
			:return: ofdm_symbols: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:OSLSubframe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.OfdmSymbols)
