from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PercentCls:
	"""Percent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("percent", core, parent)

	def set(self, cell_name: str, percent: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BLER:DL:PERCent \n
		Snippet: driver.configure.signaling.nradio.cell.bler.downlink.percent.set(cell_name = 'abc', percent = 1.0) \n
		Configures the rate of transport block errors to be inserted into the downlink data, in percent, for the initial BWP. \n
			:param cell_name: No help available
			:param percent: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('percent', percent, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BLER:DL:PERCent {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BLER:DL:PERCent \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.bler.downlink.percent.get(cell_name = 'abc') \n
		Configures the rate of transport block errors to be inserted into the downlink data, in percent, for the initial BWP. \n
			:param cell_name: No help available
			:return: percent: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BLER:DL:PERCent? {param}')
		return Conversions.str_to_float(response)
