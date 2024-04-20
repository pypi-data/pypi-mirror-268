from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RetransmCls:
	"""Retransm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("retransm", core, parent)

	def delete(self, cell_name: str, index: int, count: int = None, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:USER:RETRansm \n
		Snippet: driver.signaling.nradio.cell.bwp.harq.uplink.user.retransm.delete(cell_name = 'abc', index = 1, count = 1, bwParts = repcap.BwParts.Default) \n
		Removes retransmissions from the retransmission configuration for user-defined UL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:param index: Index of the first retransmission to be deleted. Item 1 in the GUI corresponds to Index = 0.
			:param count: Number of retransmissions to be deleted. The default is 1.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('count', count, DataType.Integer, None, is_optional=True))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:USER:RETRansm {param}'.rstrip())
