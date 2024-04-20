from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PbtrCls:
	"""Pbtr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pbtr", core, parent)

	def set(self, cell_name: str, periodicity: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:PBTR \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.pbtr.set(cell_name = 'abc', periodicity = 1) \n
		Configures the periodicity n for subsequent random LAA bursts (a burst starts every nth subframe) . \n
			:param cell_name: No help available
			:param periodicity: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:PBTR {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:PBTR \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.pbtr.get(cell_name = 'abc') \n
		Configures the periodicity n for subsequent random LAA bursts (a burst starts every nth subframe) . \n
			:param cell_name: No help available
			:return: periodicity: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:PBTR? {param}')
		return Conversions.str_to_int(response)
