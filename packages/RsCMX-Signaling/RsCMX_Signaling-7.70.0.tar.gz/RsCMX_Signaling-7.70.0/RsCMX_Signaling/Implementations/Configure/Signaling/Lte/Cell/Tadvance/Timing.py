from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimingCls:
	"""Timing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	def set(self, cell_name: str, ta: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TADVance:TIMing \n
		Snippet: driver.configure.signaling.lte.cell.tadvance.timing.set(cell_name = 'abc', ta = 1) \n
		Configures a timing advance value to be sent to the UE. \n
			:param cell_name: No help available
			:param ta: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ta', ta, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:TADVance:TIMing {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TADVance:TIMing \n
		Snippet: value: int = driver.configure.signaling.lte.cell.tadvance.timing.get(cell_name = 'abc') \n
		Configures a timing advance value to be sent to the UE. \n
			:param cell_name: No help available
			:return: ta: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:TADVance:TIMing? {param}')
		return Conversions.str_to_int(response)
