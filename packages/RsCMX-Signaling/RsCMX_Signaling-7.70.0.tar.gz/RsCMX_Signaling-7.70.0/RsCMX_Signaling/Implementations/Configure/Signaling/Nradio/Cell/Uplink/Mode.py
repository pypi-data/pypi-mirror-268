from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.ConfigMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UL:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.uplink.mode.set(cell_name = 'abc', mode = enums.ConfigMode.AUTO) \n
		Selects a configuration mode for the UL BWP settings in FDD, for the initial BWP. \n
			:param cell_name: No help available
			:param mode: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ConfigMode))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UL:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ConfigMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UL:MODE \n
		Snippet: value: enums.ConfigMode = driver.configure.signaling.nradio.cell.uplink.mode.get(cell_name = 'abc') \n
		Selects a configuration mode for the UL BWP settings in FDD, for the initial BWP. \n
			:param cell_name: No help available
			:return: mode: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UL:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ConfigMode)
