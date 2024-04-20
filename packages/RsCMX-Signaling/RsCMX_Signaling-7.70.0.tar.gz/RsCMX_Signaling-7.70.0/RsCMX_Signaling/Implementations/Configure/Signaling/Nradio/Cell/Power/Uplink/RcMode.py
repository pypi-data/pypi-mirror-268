from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcModeCls:
	"""RcMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcMode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:RCMode \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.rcMode.set(cell_name = 'abc', mode = enums.ModeB.AUTO) \n
		Selects a configuration mode for the expected UL level. \n
			:param cell_name: No help available
			:param mode: Automatic configuration or user-defined configuration
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeB))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:RCMode {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:RCMode \n
		Snippet: value: enums.ModeB = driver.configure.signaling.nradio.cell.power.uplink.rcMode.get(cell_name = 'abc') \n
		Selects a configuration mode for the expected UL level. \n
			:param cell_name: No help available
			:return: mode: Automatic configuration or user-defined configuration"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:RCMode? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeB)
