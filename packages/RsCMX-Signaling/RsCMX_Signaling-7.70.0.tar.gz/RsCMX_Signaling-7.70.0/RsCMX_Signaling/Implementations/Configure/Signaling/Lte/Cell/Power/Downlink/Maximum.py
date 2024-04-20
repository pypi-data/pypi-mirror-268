from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def set(self, cell_name: str, max_cell_power: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:MAXimum \n
		Snippet: driver.configure.signaling.lte.cell.power.downlink.maximum.set(cell_name = 'abc', max_cell_power = 1.0) \n
		Defines the maximum cell power. \n
			:param cell_name: No help available
			:param max_cell_power: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('max_cell_power', max_cell_power, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:MAXimum {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:MAXimum \n
		Snippet: value: float = driver.configure.signaling.lte.cell.power.downlink.maximum.get(cell_name = 'abc') \n
		Defines the maximum cell power. \n
			:param cell_name: No help available
			:return: max_cell_power: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:MAXimum? {param}')
		return Conversions.str_to_float(response)
