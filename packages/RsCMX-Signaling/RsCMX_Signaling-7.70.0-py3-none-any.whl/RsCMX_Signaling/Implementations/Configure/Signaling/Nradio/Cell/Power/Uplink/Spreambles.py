from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpreamblesCls:
	"""Spreambles commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spreambles", core, parent)

	def set(self, cell_name: str, start_preambles: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:SPReambles \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.spreambles.set(cell_name = 'abc', start_preambles = 1) \n
		Sets the parameter 'startPreambleForThisPartition-r17', signaled in 'FeatureCombinationPreambles-r17' to the UE. \n
			:param cell_name: No help available
			:param start_preambles: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('start_preambles', start_preambles, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:SPReambles {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:SPReambles \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.power.uplink.spreambles.get(cell_name = 'abc') \n
		Sets the parameter 'startPreambleForThisPartition-r17', signaled in 'FeatureCombinationPreambles-r17' to the UE. \n
			:param cell_name: No help available
			:return: start_preambles: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:SPReambles? {param}')
		return Conversions.str_to_int(response)
