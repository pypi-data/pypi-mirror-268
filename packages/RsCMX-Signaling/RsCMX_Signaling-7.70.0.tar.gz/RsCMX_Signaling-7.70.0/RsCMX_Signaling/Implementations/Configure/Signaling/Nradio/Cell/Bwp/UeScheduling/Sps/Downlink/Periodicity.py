from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, cell_name: str, periodicity: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:DL:PERiodicity \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.periodicity.set(cell_name = 'abc', periodicity = 1, bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'periodicity' for DL SPS scheduling, in ms, for BWP <bb>. \n
			:param cell_name: No help available
			:param periodicity: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:DL:PERiodicity {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:DL:PERiodicity \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.periodicity.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'periodicity' for DL SPS scheduling, in ms, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: periodicity: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:DL:PERiodicity? {param}')
		return Conversions.str_to_int(response)
