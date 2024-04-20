from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BehaviorCls:
	"""Behavior commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("behavior", core, parent)

	def set(self, cell_name: str, re_tx_behavior: enums.ReTxBehaviorB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RETX:BEHavior \n
		Snippet: driver.configure.signaling.lte.cell.harq.downlink.reTx.behavior.set(cell_name = 'abc', re_tx_behavior = enums.ReTxBehaviorB.CONTinue) \n
		Defines a stop condition for retransmissions. \n
			:param cell_name: No help available
			:param re_tx_behavior:
				- CONTinue: Send the maximum number of retransmissions.
				- STOP: Stop sending retransmissions when the UE answers with an ACK.
				- SNDMimo: Stop sending retransmissions when the UE answers with an ACK. For MIMO with two transport blocks, send no new data until HARQ for both transport blocks is complete (ACK or maximum retransmissions reached) .
				- SDTX: Stop sending retransmissions when DTX happens in the uplink."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('re_tx_behavior', re_tx_behavior, DataType.Enum, enums.ReTxBehaviorB))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RETX:BEHavior {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ReTxBehaviorB:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RETX:BEHavior \n
		Snippet: value: enums.ReTxBehaviorB = driver.configure.signaling.lte.cell.harq.downlink.reTx.behavior.get(cell_name = 'abc') \n
		Defines a stop condition for retransmissions. \n
			:param cell_name: No help available
			:return: re_tx_behavior:
				- CONTinue: Send the maximum number of retransmissions.
				- STOP: Stop sending retransmissions when the UE answers with an ACK.
				- SNDMimo: Stop sending retransmissions when the UE answers with an ACK. For MIMO with two transport blocks, send no new data until HARQ for both transport blocks is complete (ACK or maximum retransmissions reached) .
				- SDTX: Stop sending retransmissions when DTX happens in the uplink."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RETX:BEHavior? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ReTxBehaviorB)
