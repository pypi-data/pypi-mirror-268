from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AoaCls:
	"""Aoa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aoa", core, parent)

	def set(self, cell_name: str, aoa: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:AOA \n
		Snippet: driver.configure.signaling.nradio.cell.mconfig.aoa.set(cell_name = 'abc', aoa = 1) \n
		Selects the maximum number of emulated angles of arrival. \n
			:param cell_name: No help available
			:param aoa: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('aoa', aoa, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:AOA {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:AOA \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.mconfig.aoa.get(cell_name = 'abc') \n
		Selects the maximum number of emulated angles of arrival. \n
			:param cell_name: No help available
			:return: aoa: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:AOA? {param}')
		return Conversions.str_to_int(response)
