from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinOffsetCls:
	"""MinOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minOffset", core, parent)

	def set(self, cell_name: str, offset: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:USER:MINoffset \n
		Snippet: driver.configure.signaling.nradio.cell.harq.downlink.user.minOffset.set(cell_name = 'abc', offset = 1) \n
		Defines the minimum offset for user-defined DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:param offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('offset', offset, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:USER:MINoffset {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:USER:MINoffset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.harq.downlink.user.minOffset.get(cell_name = 'abc') \n
		Defines the minimum offset for user-defined DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:return: offset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:USER:MINoffset? {param}')
		return Conversions.str_to_int(response)
