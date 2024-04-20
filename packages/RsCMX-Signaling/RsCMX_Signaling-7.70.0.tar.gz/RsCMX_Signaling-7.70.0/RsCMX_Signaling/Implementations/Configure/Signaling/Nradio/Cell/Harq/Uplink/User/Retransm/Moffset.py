from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MoffsetCls:
	"""Moffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("moffset", core, parent)

	def set(self, cell_name: str, index: int, minimum_offset: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:MOFFset \n
		Snippet: driver.configure.signaling.nradio.cell.harq.uplink.user.retransm.moffset.set(cell_name = 'abc', index = 1, minimum_offset = 1) \n
		Minimum number of slots between feedback processing and sending the retransmission DCI, for the initial BWP. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param minimum_offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('minimum_offset', minimum_offset, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:MOFFset {param}'.rstrip())

	def get(self, cell_name: str, index: int) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:MOFFset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.harq.uplink.user.retransm.moffset.get(cell_name = 'abc', index = 1) \n
		Minimum number of slots between feedback processing and sending the retransmission DCI, for the initial BWP. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:return: minimum_offset: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:MOFFset? {param}'.rstrip())
		return Conversions.str_to_int(response)
