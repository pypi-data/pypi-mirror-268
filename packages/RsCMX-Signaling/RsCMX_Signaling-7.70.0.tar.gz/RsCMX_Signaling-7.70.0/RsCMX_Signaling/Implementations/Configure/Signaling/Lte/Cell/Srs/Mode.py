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

	def set(self, cell_name: str, mode: enums.ModeSrs) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:SRS:MODE \n
		Snippet: driver.configure.signaling.lte.cell.srs.mode.set(cell_name = 'abc', mode = enums.ModeSrs.A508) \n
		Selects whether SRS is supported by the cell and via which method the signaled SRS parameters are configured. \n
			:param cell_name: No help available
			:param mode: OFF: no SRS parameters signaled to UE UDEFined: configuration of SRS parameters via other commands in this chapter A508: automatic configuration according to 3GPP TS 36.508 A521: automatic configuration according to 3GPP TS 36.521
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeSrs))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:SRS:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeSrs:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:SRS:MODE \n
		Snippet: value: enums.ModeSrs = driver.configure.signaling.lte.cell.srs.mode.get(cell_name = 'abc') \n
		Selects whether SRS is supported by the cell and via which method the signaled SRS parameters are configured. \n
			:param cell_name: No help available
			:return: mode: OFF: no SRS parameters signaled to UE UDEFined: configuration of SRS parameters via other commands in this chapter A508: automatic configuration according to 3GPP TS 36.508 A521: automatic configuration according to 3GPP TS 36.521"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:SRS:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeSrs)
