from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmodeCls:
	"""Smode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeUeScheduling, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SMODe \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.smode.set(cell_name = 'abc', mode = enums.ModeUeScheduling.BO, bwParts = repcap.BwParts.Default) \n
		Selects a scheduling mode for DL and UL, for BWP <bb>. \n
			:param cell_name: No help available
			:param mode: FIXed: Fixed scheduling, DL and UL. SPS: SPS DL, CG UL. CQI: Follow CQI WB DL, fixed scheduling UL. PRI: Follow PMI WB + RI DL, fixed scheduling UL. CPRI: Follow CQI WB + PMI WB + RI DL, fixed scheduling UL. BO: Follow buffer occupancy (BO) DL, fixed scheduling UL. UDEFined: Other dynamic scheduling mode (query only) .
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeUeScheduling))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.ModeUeScheduling:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SMODe \n
		Snippet: value: enums.ModeUeScheduling = driver.configure.signaling.nradio.cell.bwp.ueScheduling.smode.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects a scheduling mode for DL and UL, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mode: FIXed: Fixed scheduling, DL and UL. SPS: SPS DL, CG UL. CQI: Follow CQI WB DL, fixed scheduling UL. PRI: Follow PMI WB + RI DL, fixed scheduling UL. CPRI: Follow CQI WB + PMI WB + RI DL, fixed scheduling UL. BO: Follow buffer occupancy (BO) DL, fixed scheduling UL. UDEFined: Other dynamic scheduling mode (query only) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeUeScheduling)
