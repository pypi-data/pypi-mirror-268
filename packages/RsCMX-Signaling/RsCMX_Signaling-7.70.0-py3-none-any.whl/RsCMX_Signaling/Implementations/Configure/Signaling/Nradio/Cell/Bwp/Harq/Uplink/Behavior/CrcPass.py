from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrcPassCls:
	"""CrcPass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crcPass", core, parent)

	def set(self, cell_name: str, behavior: enums.AckOrDtx, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:BEHavior:CRCPass \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.harq.uplink.behavior.crcPass.set(cell_name = 'abc', behavior = enums.AckOrDtx.CONTinue, bwParts = repcap.BwParts.Default) \n
		Defines the behavior when a UL transmission passes the CRC check: stop or continue requesting retransmissions from the UE,
		for BWP <bb>. \n
			:param cell_name: No help available
			:param behavior: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('behavior', behavior, DataType.Enum, enums.AckOrDtx))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:BEHavior:CRCPass {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.AckOrDtx:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:BEHavior:CRCPass \n
		Snippet: value: enums.AckOrDtx = driver.configure.signaling.nradio.cell.bwp.harq.uplink.behavior.crcPass.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines the behavior when a UL transmission passes the CRC check: stop or continue requesting retransmissions from the UE,
		for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: behavior: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:BEHavior:CRCPass? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AckOrDtx)
