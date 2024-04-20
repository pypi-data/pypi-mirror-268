from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, cell_name: str, periodicity: enums.SpsPeriodicity) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:PERiodicity \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.periodicity.set(cell_name = 'abc', periodicity = enums.SpsPeriodicity.S1) \n
		Configures the signaled 'periodicity' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:param periodicity: SYMn: n symbols Sn: n slots S1K, S1K2, S2K, S5K: 1024, 1280, 2560, 5120 slots
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Enum, enums.SpsPeriodicity))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:PERiodicity {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.SpsPeriodicity:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:PERiodicity \n
		Snippet: value: enums.SpsPeriodicity = driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.periodicity.get(cell_name = 'abc') \n
		Configures the signaled 'periodicity' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: periodicity: SYMn: n symbols Sn: n slots S1K, S1K2, S2K, S5K: 1024, 1280, 2560, 5120 slots"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:PERiodicity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SpsPeriodicity)
