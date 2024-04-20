from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:DL:USER:RETRansm:COUNt \n
		Snippet: value: int = driver.sense.signaling.nradio.cell.bwp.harq.downlink.user.retransm.count.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Queries the number of DL retransmissions for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: retransmissions: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:DL:USER:RETRansm:COUNt? {param}')
		return Conversions.str_to_int(response)
