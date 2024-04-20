from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AportsCls:
	"""Aports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aports", core, parent)

	def set(self, cell_name: str, ul_antenna_ports: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:APORts \n
		Snippet: driver.configure.signaling.nradio.cell.mconfig.aports.set(cell_name = 'abc', ul_antenna_ports = 1) \n
		Selects the maximum number of UL antenna ports at the instrument side, allowed in live mode. \n
			:param cell_name: No help available
			:param ul_antenna_ports: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ul_antenna_ports', ul_antenna_ports, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:APORts {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:APORts \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.mconfig.aports.get(cell_name = 'abc') \n
		Selects the maximum number of UL antenna ports at the instrument side, allowed in live mode. \n
			:param cell_name: No help available
			:return: ul_antenna_ports: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:APORts? {param}')
		return Conversions.str_to_int(response)
