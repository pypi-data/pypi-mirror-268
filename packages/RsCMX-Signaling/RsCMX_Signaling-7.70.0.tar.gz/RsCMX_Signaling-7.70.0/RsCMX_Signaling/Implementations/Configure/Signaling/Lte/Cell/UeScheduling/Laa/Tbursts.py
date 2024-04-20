from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TburstsCls:
	"""Tbursts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbursts", core, parent)

	def set(self, cell_name: str, burst_type: enums.BurstType) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:TBURsts \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.tbursts.set(cell_name = 'abc', burst_type = enums.BurstType.FBURst) \n
		Selects the burst type for LAA. \n
			:param cell_name: No help available
			:param burst_type: Fixed bursts or random bursts
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('burst_type', burst_type, DataType.Enum, enums.BurstType))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:TBURsts {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.BurstType:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:TBURsts \n
		Snippet: value: enums.BurstType = driver.configure.signaling.lte.cell.ueScheduling.laa.tbursts.get(cell_name = 'abc') \n
		Selects the burst type for LAA. \n
			:param cell_name: No help available
			:return: burst_type: Fixed bursts or random bursts"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:TBURsts? {param}')
		return Conversions.str_to_scalar_enum(response, enums.BurstType)
