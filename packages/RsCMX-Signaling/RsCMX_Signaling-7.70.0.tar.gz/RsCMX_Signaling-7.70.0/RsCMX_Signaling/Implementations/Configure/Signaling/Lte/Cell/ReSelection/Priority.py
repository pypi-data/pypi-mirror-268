from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PriorityCls:
	"""Priority commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("priority", core, parent)

	def set(self, cell_name: str, priority: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RESelection:PRIority \n
		Snippet: driver.configure.signaling.lte.cell.reSelection.priority.set(cell_name = 'abc', priority = 1.0) \n
		Configures the parameter 'cellReselectionPriority', signaled to the UE in SIB3. \n
			:param cell_name: No help available
			:param priority: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('priority', priority, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RESelection:PRIority {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RESelection:PRIority \n
		Snippet: value: float = driver.configure.signaling.lte.cell.reSelection.priority.get(cell_name = 'abc') \n
		Configures the parameter 'cellReselectionPriority', signaled to the UE in SIB3. \n
			:param cell_name: No help available
			:return: priority: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RESelection:PRIority? {param}')
		return Conversions.str_to_float(response)
