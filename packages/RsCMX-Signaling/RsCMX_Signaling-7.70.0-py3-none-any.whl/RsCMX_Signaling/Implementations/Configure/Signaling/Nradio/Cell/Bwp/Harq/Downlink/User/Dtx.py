from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtxCls:
	"""Dtx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtx", core, parent)

	def set(self, cell_name: str, dtx: enums.AckOrDtx, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:DL:USER:DTX \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.harq.downlink.user.dtx.set(cell_name = 'abc', dtx = enums.AckOrDtx.CONTinue, bwParts = repcap.BwParts.Default) \n
		Defines the reaction to DTX (missing ACKs) , for user-defined DL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param dtx: STOP: stop retransmitting CONTinue: continue retransmitting
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('dtx', dtx, DataType.Enum, enums.AckOrDtx))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:DL:USER:DTX {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.AckOrDtx:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:DL:USER:DTX \n
		Snippet: value: enums.AckOrDtx = driver.configure.signaling.nradio.cell.bwp.harq.downlink.user.dtx.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines the reaction to DTX (missing ACKs) , for user-defined DL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: dtx: STOP: stop retransmitting CONTinue: continue retransmitting"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:DL:USER:DTX? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AckOrDtx)
