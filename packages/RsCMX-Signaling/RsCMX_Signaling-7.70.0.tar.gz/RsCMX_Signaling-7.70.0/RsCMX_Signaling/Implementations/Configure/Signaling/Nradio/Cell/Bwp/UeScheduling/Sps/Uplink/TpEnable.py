from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpEnableCls:
	"""TpEnable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpEnable", core, parent)

	def set(self, cell_name: str, enable_tp: bool, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:UL:TPENable \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.uplink.tpEnable.set(cell_name = 'abc', enable_tp = False, bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'transformPrecoder' for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param enable_tp: ON: DFT-s-OFDM (with transform precoding) . OFF: CP-OFDM (no transform precoding) .
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable_tp', enable_tp, DataType.Boolean))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:UL:TPENable {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:UL:TPENable \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.uplink.tpEnable.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'transformPrecoder' for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: enable_tp: ON: DFT-s-OFDM (with transform precoding) . OFF: CP-OFDM (no transform precoding) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:UL:TPENable? {param}')
		return Conversions.str_to_bool(response)
