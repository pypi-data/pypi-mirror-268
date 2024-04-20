from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmodeCls:
	"""Smode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeS) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:SMODe \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.uplink.smode.set(cell_name = 'abc', mode = enums.ModeS.FIXed) \n
		Selects a scheduling mode for the UL. \n
			:param cell_name: No help available
			:param mode: FIXed: Fixed scheduling SPS: Semi-persistent scheduling SRBSr: Follow SR/BSR UDEFined: Other scheduling mode (query only) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeS))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:SMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeS:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:SMODe \n
		Snippet: value: enums.ModeS = driver.configure.signaling.lte.cell.ueScheduling.uplink.smode.get(cell_name = 'abc') \n
		Selects a scheduling mode for the UL. \n
			:param cell_name: No help available
			:return: mode: FIXed: Fixed scheduling SPS: Semi-persistent scheduling SRBSr: Follow SR/BSR UDEFined: Other scheduling mode (query only) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:SMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeS)
