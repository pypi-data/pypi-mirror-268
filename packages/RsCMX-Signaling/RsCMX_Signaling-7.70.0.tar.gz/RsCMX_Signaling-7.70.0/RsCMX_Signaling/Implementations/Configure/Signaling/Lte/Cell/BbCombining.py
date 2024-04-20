from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbCombiningCls:
	"""BbCombining commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbCombining", core, parent)

	def set(self, cell_name: str, enable: bool) -> None:
		"""SCPI: [CONfigure]:SIGNaling:LTE:CELL:BBCombining \n
		Snippet: driver.configure.signaling.lte.cell.bbCombining.set(cell_name = 'abc', enable = False) \n
		Allows baseband combining for the cell. \n
			:param cell_name: No help available
			:param enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONfigure:SIGNaling:LTE:CELL:BBCombining {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONfigure]:SIGNaling:LTE:CELL:BBCombining \n
		Snippet: value: bool = driver.configure.signaling.lte.cell.bbCombining.get(cell_name = 'abc') \n
		Allows baseband combining for the cell. \n
			:param cell_name: No help available
			:return: enable: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONfigure:SIGNaling:LTE:CELL:BBCombining? {param}')
		return Conversions.str_to_bool(response)
