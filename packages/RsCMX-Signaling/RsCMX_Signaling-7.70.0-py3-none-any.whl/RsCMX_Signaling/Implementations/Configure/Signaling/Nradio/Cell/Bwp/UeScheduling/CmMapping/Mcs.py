from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsCls:
	"""Mcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcs", core, parent)

	def set(self, cell_name: str, mcs: List[int], bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:CMMapping:MCS \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.cmMapping.mcs.set(cell_name = 'abc', mcs = [1, 2, 3], bwParts = repcap.BwParts.Default) \n
		Sets the configuration mode to UDEFined and defines the mapping table for that mode, for BWP <bb>. A query returns the
		mapping table contents for the currently used configuration mode, without changing the mode.
		For setting the configuration mode, see [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCSTable. \n
			:param cell_name: No help available
			:param mcs: Comma-separated list of 16 MCS values, for reported CQI values 0 to 15.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs', mcs, DataType.IntegerList, None, False, False, 16))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:CMMapping:MCS {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> List[int]:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:CMMapping:MCS \n
		Snippet: value: List[int] = driver.configure.signaling.nradio.cell.bwp.ueScheduling.cmMapping.mcs.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Sets the configuration mode to UDEFined and defines the mapping table for that mode, for BWP <bb>. A query returns the
		mapping table contents for the currently used configuration mode, without changing the mode.
		For setting the configuration mode, see [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCSTable. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mcs: Comma-separated list of 16 MCS values, for reported CQI values 0 to 15."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_bin_or_ascii_int_list(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:CMMapping:MCS? {param}')
		return response
