from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmodeCls:
	"""Cmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmode", core, parent)

	def set(self, cell_name: str, config_mode: enums.ConfigMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:CMODe \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.cmode.set(cell_name = 'abc', config_mode = enums.ConfigMode.AUTO) \n
		Selects a configuration mode for the expected UL level. \n
			:param cell_name: No help available
			:param config_mode: Automatic configuration or user-defined configuration
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('config_mode', config_mode, DataType.Enum, enums.ConfigMode))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:CMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ConfigMode:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:CMODe \n
		Snippet: value: enums.ConfigMode = driver.configure.signaling.lte.cell.power.uplink.cmode.get(cell_name = 'abc') \n
		Selects a configuration mode for the expected UL level. \n
			:param cell_name: No help available
			:return: config_mode: Automatic configuration or user-defined configuration"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:CMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ConfigMode)
