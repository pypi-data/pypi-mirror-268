from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SepreCls:
	"""Sepre commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sepre", core, parent)

	def set(self, cell_name: str, epre: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:SEPRe \n
		Snippet: driver.configure.signaling.nradio.cell.power.downlink.sepre.set(cell_name = 'abc', epre = 1.0) \n
		Defines the SSB EPRE. \n
			:param cell_name: No help available
			:param epre: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('epre', epre, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:SEPRe {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:SEPRe \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.power.downlink.sepre.get(cell_name = 'abc') \n
		Defines the SSB EPRE. \n
			:param cell_name: No help available
			:return: epre: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:SEPRe? {param}')
		return Conversions.str_to_float(response)
