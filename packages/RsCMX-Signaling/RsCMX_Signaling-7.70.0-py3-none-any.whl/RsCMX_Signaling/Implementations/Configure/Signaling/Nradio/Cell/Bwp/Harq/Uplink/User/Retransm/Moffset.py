from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MoffsetCls:
	"""Moffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("moffset", core, parent)

	def set(self, cell_name: str, index: int, minimum_offset: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:USER:RETRansm:MOFFset \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.harq.uplink.user.retransm.moffset.set(cell_name = 'abc', index = 1, minimum_offset = 1, bwParts = repcap.BwParts.Default) \n
		Minimum number of slots between feedback processing and sending the retransmission DCI, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param minimum_offset: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('minimum_offset', minimum_offset, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:USER:RETRansm:MOFFset {param}'.rstrip())

	def get(self, cell_name: str, index: int, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:USER:RETRansm:MOFFset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.bwp.harq.uplink.user.retransm.moffset.get(cell_name = 'abc', index = 1, bwParts = repcap.BwParts.Default) \n
		Minimum number of slots between feedback processing and sending the retransmission DCI, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: minimum_offset: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:USER:RETRansm:MOFFset? {param}'.rstrip())
		return Conversions.str_to_int(response)
