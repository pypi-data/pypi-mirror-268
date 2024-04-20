from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchCls:
	"""Pdcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	def set(self, cell_name: str, no_symbols: enums.NoSymbols) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:PDCCh \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.userDefined.pdcch.set(cell_name = 'abc', no_symbols = enums.NoSymbols.S1) \n
		Configures the number of OFDM symbols used for the PDCCH. \n
			:param cell_name: No help available
			:param no_symbols: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('no_symbols', no_symbols, DataType.Enum, enums.NoSymbols))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:PDCCh {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.NoSymbols:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:PDCCh \n
		Snippet: value: enums.NoSymbols = driver.configure.signaling.lte.cell.ueScheduling.userDefined.pdcch.get(cell_name = 'abc') \n
		Configures the number of OFDM symbols used for the PDCCH. \n
			:param cell_name: No help available
			:return: no_symbols: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:PDCCh? {param}')
		return Conversions.str_to_scalar_enum(response, enums.NoSymbols)
