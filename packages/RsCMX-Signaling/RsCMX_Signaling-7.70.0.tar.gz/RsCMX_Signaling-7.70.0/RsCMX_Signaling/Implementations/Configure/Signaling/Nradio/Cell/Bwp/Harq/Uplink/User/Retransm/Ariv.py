from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ArivCls:
	"""Ariv commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ariv", core, parent)

	def set(self, cell_name: str, index: int, riv: bool, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:USER:RETRansm:ARIV \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.harq.uplink.user.retransm.ariv.set(cell_name = 'abc', index = 1, riv = False, bwParts = repcap.BwParts.Default) \n
		Configures auto RIV for a certain retransmission, for user-defined UL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param riv: ON: Auto RIV enabled, no. of RB and start RB set automatically. OFF: Auto RIV disabled, you can define no. of RB and start RB.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('riv', riv, DataType.Boolean))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:USER:RETRansm:ARIV {param}'.rstrip())

	def get(self, cell_name: str, index: int, bwParts=repcap.BwParts.Default) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:USER:RETRansm:ARIV \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.bwp.harq.uplink.user.retransm.ariv.get(cell_name = 'abc', index = 1, bwParts = repcap.BwParts.Default) \n
		Configures auto RIV for a certain retransmission, for user-defined UL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: riv: ON: Auto RIV enabled, no. of RB and start RB set automatically. OFF: Auto RIV disabled, you can define no. of RB and start RB."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:USER:RETRansm:ARIV? {param}'.rstrip())
		return Conversions.str_to_bool(response)
