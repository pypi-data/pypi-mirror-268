from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RetransmCls:
	"""Retransm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("retransm", core, parent)

	def set(self, cell_name: str, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: ADD:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:DL:USER:RETRansm \n
		Snippet: driver.add.signaling.nradio.cell.bwp.harq.downlink.user.retransm.set(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Adds a retransmission to the retransmission configuration for user-defined DL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'ADD:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:DL:USER:RETRansm {param}')
