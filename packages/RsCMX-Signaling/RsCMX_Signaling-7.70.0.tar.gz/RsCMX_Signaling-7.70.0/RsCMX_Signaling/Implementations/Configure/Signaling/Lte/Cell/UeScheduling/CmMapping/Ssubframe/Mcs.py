from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsCls:
	"""Mcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcs", core, parent)

	def set(self, cell_name: str, mcs: List[int]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:CMMapping:SSUBframe:MCS \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.cmMapping.ssubframe.mcs.set(cell_name = 'abc', mcs = [1, 2, 3]) \n
		Sets the configuration mode to UDEFined and defines the mapping table for that mode. A query returns the mapping table
		contents for the currently used configuration mode, without changing the mode. For setting the configuration mode, see
		[CONFigure:]SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCSTable. There is a configuration mode and a mapping table
		for each type of DL subframe: CSI-RS subframe (CSIRs) , special subframe for TDD (SSUBframe) , all other subframes
		(NSUBframe) . \n
			:param cell_name: No help available
			:param mcs: Comma-separated list of 16 MCS values, for reported CQI values 0 to 15.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs', mcs, DataType.IntegerList, None, False, False, 16))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:CMMapping:SSUBframe:MCS {param}'.rstrip())

	def get(self, cell_name: str) -> List[int]:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:CMMapping:SSUBframe:MCS \n
		Snippet: value: List[int] = driver.configure.signaling.lte.cell.ueScheduling.cmMapping.ssubframe.mcs.get(cell_name = 'abc') \n
		Sets the configuration mode to UDEFined and defines the mapping table for that mode. A query returns the mapping table
		contents for the currently used configuration mode, without changing the mode. For setting the configuration mode, see
		[CONFigure:]SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCSTable. There is a configuration mode and a mapping table
		for each type of DL subframe: CSI-RS subframe (CSIRs) , special subframe for TDD (SSUBframe) , all other subframes
		(NSUBframe) . \n
			:param cell_name: No help available
			:return: mcs: Comma-separated list of 16 MCS values, for reported CQI values 0 to 15."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_bin_or_ascii_int_list(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:CMMapping:SSUBframe:MCS? {param}')
		return response
