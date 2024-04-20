from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, cell_name: str, state: bool) -> None:
		"""SCPI: SOURce:SIGNaling:NRADio:CELL:STATe \n
		Snippet: driver.source.signaling.nradio.cell.state.set(cell_name = 'abc', state = False) \n
		Turns the cell signal on or off. \n
			:param cell_name: No help available
			:param state: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('state', state, DataType.Boolean))
		self._core.io.write(f'SOURce:SIGNaling:NRADio:CELL:STATe {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: SOURce:SIGNaling:NRADio:CELL:STATe \n
		Snippet: value: bool = driver.source.signaling.nradio.cell.state.get(cell_name = 'abc') \n
		Turns the cell signal on or off. \n
			:param cell_name: No help available
			:return: state: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SOURce:SIGNaling:NRADio:CELL:STATe? {param}')
		return Conversions.str_to_bool(response)
