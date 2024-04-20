from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CycleCls:
	"""Cycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cycle", core, parent)

	def set(self, cell_name: str, cycle: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:LDRX:CYCLe \n
		Snippet: driver.configure.signaling.nradio.cell.cdrx.ldrx.cycle.set(cell_name = 'abc', cycle = 1) \n
		Configures the duration of one long DRX cycle. The long DRX cycle duration must be divisible by the short DRX cycle
		duration. \n
			:param cell_name: No help available
			:param cycle: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('cycle', cycle, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:LDRX:CYCLe {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:LDRX:CYCLe \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.cdrx.ldrx.cycle.get(cell_name = 'abc') \n
		Configures the duration of one long DRX cycle. The long DRX cycle duration must be divisible by the short DRX cycle
		duration. \n
			:param cell_name: No help available
			:return: cycle: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:LDRX:CYCLe? {param}')
		return Conversions.str_to_int(response)
