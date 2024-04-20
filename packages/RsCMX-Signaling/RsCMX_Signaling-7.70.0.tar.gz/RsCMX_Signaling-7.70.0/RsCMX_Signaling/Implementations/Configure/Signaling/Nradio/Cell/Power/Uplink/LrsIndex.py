from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrsIndexCls:
	"""LrsIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrsIndex", core, parent)

	def set(self, cell_name: str, index: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:LRSindex \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.lrsIndex.set(cell_name = 'abc', index = 1) \n
		Sets the parameter 'prach-RootSequenceIndex', signaled to the UE. \n
			:param cell_name: No help available
			:param index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:LRSindex {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:LRSindex \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.power.uplink.lrsIndex.get(cell_name = 'abc') \n
		Sets the parameter 'prach-RootSequenceIndex', signaled to the UE. \n
			:param cell_name: No help available
			:return: index: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:LRSindex? {param}')
		return Conversions.str_to_int(response)
