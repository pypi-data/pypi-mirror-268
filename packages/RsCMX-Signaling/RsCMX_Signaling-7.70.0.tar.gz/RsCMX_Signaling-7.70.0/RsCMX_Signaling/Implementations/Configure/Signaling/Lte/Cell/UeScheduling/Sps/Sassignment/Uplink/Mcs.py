from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsCls:
	"""Mcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcs", core, parent)

	def set(self, cell_name: str, mcs: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:MCS \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.mcs.set(cell_name = 'abc', mcs = 1) \n
		Specifies the MCS index for SPS UL scheduling. \n
			:param cell_name: No help available
			:param mcs: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs', mcs, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:MCS {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:MCS \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.mcs.get(cell_name = 'abc') \n
		Specifies the MCS index for SPS UL scheduling. \n
			:param cell_name: No help available
			:return: mcs: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:MCS? {param}')
		return Conversions.str_to_int(response)
