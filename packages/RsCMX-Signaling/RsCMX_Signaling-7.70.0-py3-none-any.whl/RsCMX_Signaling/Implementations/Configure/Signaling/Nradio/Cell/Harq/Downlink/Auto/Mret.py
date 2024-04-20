from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MretCls:
	"""Mret commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mret", core, parent)

	def set(self, cell_name: str, retransmissions: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:AUTO:MRET \n
		Snippet: driver.configure.signaling.nradio.cell.harq.downlink.auto.mret.set(cell_name = 'abc', retransmissions = 1) \n
		Configures the maximum number of retransmissions, for auto-configured DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:param retransmissions: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('retransmissions', retransmissions, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:AUTO:MRET {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:DL:AUTO:MRET \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.harq.downlink.auto.mret.get(cell_name = 'abc') \n
		Configures the maximum number of retransmissions, for auto-configured DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
			:return: retransmissions: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:DL:AUTO:MRET? {param}')
		return Conversions.str_to_int(response)
