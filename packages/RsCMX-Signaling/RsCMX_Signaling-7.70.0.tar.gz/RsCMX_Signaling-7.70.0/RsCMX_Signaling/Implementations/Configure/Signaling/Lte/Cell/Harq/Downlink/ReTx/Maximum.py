from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def set(self, cell_name: str, max_re_tx: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RETX:MAXimum \n
		Snippet: driver.configure.signaling.lte.cell.harq.downlink.reTx.maximum.set(cell_name = 'abc', max_re_tx = 1) \n
		Configures the maximum number of DL retransmissions. \n
			:param cell_name: No help available
			:param max_re_tx: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('max_re_tx', max_re_tx, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RETX:MAXimum {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RETX:MAXimum \n
		Snippet: value: int = driver.configure.signaling.lte.cell.harq.downlink.reTx.maximum.get(cell_name = 'abc') \n
		Configures the maximum number of DL retransmissions. \n
			:param cell_name: No help available
			:return: max_re_tx: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RETX:MAXimum? {param}')
		return Conversions.str_to_int(response)
