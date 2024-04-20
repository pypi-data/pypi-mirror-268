from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsRsOffsetCls:
	"""PsRsOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psRsOffset", core, parent)

	def set(self, cell_name: str, ps_rs_offset: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:PSRSoffset \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.psRsOffset.set(cell_name = 'abc', ps_rs_offset = 1) \n
		Sets the parameter 'pSRS-Offset', signaled to the UE as an uplink power control parameter. \n
			:param cell_name: No help available
			:param ps_rs_offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ps_rs_offset', ps_rs_offset, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:PSRSoffset {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:PSRSoffset \n
		Snippet: value: int = driver.configure.signaling.lte.cell.power.uplink.psRsOffset.get(cell_name = 'abc') \n
		Sets the parameter 'pSRS-Offset', signaled to the UE as an uplink power control parameter. \n
			:param cell_name: No help available
			:return: ps_rs_offset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:PSRSoffset? {param}')
		return Conversions.str_to_int(response)
