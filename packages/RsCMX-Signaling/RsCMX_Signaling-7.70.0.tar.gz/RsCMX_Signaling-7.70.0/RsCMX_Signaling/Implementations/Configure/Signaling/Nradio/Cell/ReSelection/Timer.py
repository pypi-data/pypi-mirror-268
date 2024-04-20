from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimerCls:
	"""Timer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timer", core, parent)

	def set(self, cell_name: str, time: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RESelection:TIMer \n
		Snippet: driver.configure.signaling.nradio.cell.reSelection.timer.set(cell_name = 'abc', time = 1) \n
		Configures the parameter 't-ReselectionNR', signaled to the UE in SIB2. \n
			:param cell_name: No help available
			:param time: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('time', time, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RESelection:TIMer {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RESelection:TIMer \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.reSelection.timer.get(cell_name = 'abc') \n
		Configures the parameter 't-ReselectionNR', signaled to the UE in SIB2. \n
			:param cell_name: No help available
			:return: time: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RESelection:TIMer? {param}')
		return Conversions.str_to_int(response)
