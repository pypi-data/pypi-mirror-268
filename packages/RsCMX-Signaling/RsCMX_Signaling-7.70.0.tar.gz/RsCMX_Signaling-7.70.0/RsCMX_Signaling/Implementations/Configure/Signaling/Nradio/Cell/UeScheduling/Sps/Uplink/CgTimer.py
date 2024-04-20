from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CgTimerCls:
	"""CgTimer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cgTimer", core, parent)

	def set(self, cell_name: str, timer: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:CGTimer \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.cgTimer.set(cell_name = 'abc', timer = 1) \n
		Configures the signaled 'configuredGrantTimer' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:param timer: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('timer', timer, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:CGTimer {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:CGTimer \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.cgTimer.get(cell_name = 'abc') \n
		Configures the signaled 'configuredGrantTimer' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: timer: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:CGTimer? {param}')
		return Conversions.str_to_int(response)
