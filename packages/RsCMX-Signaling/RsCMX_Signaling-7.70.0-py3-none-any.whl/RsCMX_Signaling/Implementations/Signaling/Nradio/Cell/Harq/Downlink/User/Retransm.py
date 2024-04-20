from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RetransmCls:
	"""Retransm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("retransm", core, parent)

	def delete(self, cell_name: str, index: int, count: int = None) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm \n
		Snippet: driver.signaling.nradio.cell.harq.downlink.user.retransm.delete(cell_name = 'abc', index = 1, count = 1) \n
		Removes retransmissions from the retransmission configuration for user-defined DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:param index: Index of the first retransmission to be deleted. Item 1 in the GUI corresponds to Index = 0.
			:param count: Number of retransmissions to be deleted. The default is 1.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('count', count, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm {param}'.rstrip())
