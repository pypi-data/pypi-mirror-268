from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HrTimerCls:
	"""HrTimer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hrTimer", core, parent)

	def set(self, cell_name: str, timer: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:UL:HRTimer \n
		Snippet: driver.configure.signaling.nradio.cell.cdrx.uplink.hrTimer.set(cell_name = 'abc', timer = 1) \n
		Configures the 'drx-HARQ-RTT-TimerUL'. \n
			:param cell_name: No help available
			:param timer: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('timer', timer, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:UL:HRTimer {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:UL:HRTimer \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.cdrx.uplink.hrTimer.get(cell_name = 'abc') \n
		Configures the 'drx-HARQ-RTT-TimerUL'. \n
			:param cell_name: No help available
			:return: timer: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:UL:HRTimer? {param}')
		return Conversions.str_to_int(response)
