from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinLevelCls:
	"""MinLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minLevel", core, parent)

	def set(self, cell_name: str, power: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RESelection:MINLevel \n
		Snippet: driver.configure.signaling.lte.cell.reSelection.minLevel.set(cell_name = 'abc', power = 1) \n
		Configures the parameter 'q-RxLevMin', signaled to the UE in SIB3. \n
			:param cell_name: No help available
			:param power: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('power', power, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RESelection:MINLevel {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RESelection:MINLevel \n
		Snippet: value: int = driver.configure.signaling.lte.cell.reSelection.minLevel.get(cell_name = 'abc') \n
		Configures the parameter 'q-RxLevMin', signaled to the UE in SIB3. \n
			:param cell_name: No help available
			:return: power: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RESelection:MINLevel? {param}')
		return Conversions.str_to_int(response)
