from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SindexCls:
	"""Sindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sindex", core, parent)

	def set(self, cell_name: str, slot: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:SINDex \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.sindex.set(cell_name = 'abc', slot = 1) \n
		Selects a slot for sending the DCI that informs the UE about the UL grant, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:SINDex {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:SINDex \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.sindex.get(cell_name = 'abc') \n
		Selects a slot for sending the DCI that informs the UE about the UL grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: slot: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:SINDex? {param}')
		return Conversions.str_to_int(response)
