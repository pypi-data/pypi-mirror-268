from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmodeCls:
	"""Smode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeUeScheduling) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SMODe \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.smode.set(cell_name = 'abc', mode = enums.ModeUeScheduling.BO) \n
		Selects a scheduling mode for DL and UL, for the initial BWP. \n
			:param cell_name: No help available
			:param mode: FIXed: Fixed scheduling, DL and UL. SPS: SPS DL, CG UL. CQI: Follow CQI WB DL, fixed scheduling UL. PRI: Follow PMI WB + RI DL, fixed scheduling UL. CPRI: Follow CQI WB + PMI WB + RI DL, fixed scheduling UL. BO: Follow buffer occupancy (BO) DL, fixed scheduling UL. UDEFined: Other dynamic scheduling mode (query only) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeUeScheduling))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeUeScheduling:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SMODe \n
		Snippet: value: enums.ModeUeScheduling = driver.configure.signaling.nradio.cell.ueScheduling.smode.get(cell_name = 'abc') \n
		Selects a scheduling mode for DL and UL, for the initial BWP. \n
			:param cell_name: No help available
			:return: mode: FIXed: Fixed scheduling, DL and UL. SPS: SPS DL, CG UL. CQI: Follow CQI WB DL, fixed scheduling UL. PRI: Follow PMI WB + RI DL, fixed scheduling UL. CPRI: Follow CQI WB + PMI WB + RI DL, fixed scheduling UL. BO: Follow buffer occupancy (BO) DL, fixed scheduling UL. UDEFined: Other dynamic scheduling mode (query only) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeUeScheduling)
