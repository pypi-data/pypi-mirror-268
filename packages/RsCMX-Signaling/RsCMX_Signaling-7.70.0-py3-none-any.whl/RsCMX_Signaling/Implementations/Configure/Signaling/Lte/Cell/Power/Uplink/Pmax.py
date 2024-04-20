from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmaxCls:
	"""Pmax commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmax", core, parent)

	def set(self, cell_name: str, power: float or bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:PMAX \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.pmax.set(cell_name = 'abc', power = 1.0) \n
		Sets the UL power control parameter 'p-Max'. \n
			:param cell_name: No help available
			:param power: (float or boolean) OFF means that the parameter is not signaled.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('power', power, DataType.FloatExt))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:PMAX {param}'.rstrip())

	def get(self, cell_name: str) -> float or bool:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:PMAX \n
		Snippet: value: float or bool = driver.configure.signaling.lte.cell.power.uplink.pmax.get(cell_name = 'abc') \n
		Sets the UL power control parameter 'p-Max'. \n
			:param cell_name: No help available
			:return: power: (float or boolean) OFF means that the parameter is not signaled."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:PMAX? {param}')
		return Conversions.str_to_float_or_bool(response)
