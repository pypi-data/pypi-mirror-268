from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsModesCls:
	"""McsModes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsModes", core, parent)

	def set(self, cell_name: str, mode: enums.McsMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCSModes \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.uplink.bsrConfig.mcsModes.set(cell_name = 'abc', mode = enums.McsMode.FIXed) \n
		Selects a mode for MCS configuration for follow BSR. \n
			:param cell_name: No help available
			:param mode:
				- MAX: The maximum MCS index is configured via [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCS.
				- FIXed: A fixed MCS index is configured via [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCS.
				- MMO: The maximum modulation scheme is configured via [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MORDer."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.McsMode))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCSModes {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.McsMode:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCSModes \n
		Snippet: value: enums.McsMode = driver.configure.signaling.lte.cell.ueScheduling.uplink.bsrConfig.mcsModes.get(cell_name = 'abc') \n
		Selects a mode for MCS configuration for follow BSR. \n
			:param cell_name: No help available
			:return: mode:
				- MAX: The maximum MCS index is configured via [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCS.
				- FIXed: A fixed MCS index is configured via [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCS.
				- MMO: The maximum modulation scheme is configured via [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MORDer."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MCSModes? {param}')
		return Conversions.str_to_scalar_enum(response, enums.McsMode)
