from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbgIndexCls:
	"""BbgIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbgIndex", core, parent)

	def get(self, cell_name: str) -> int:
		"""SCPI: SENSe:SIGNaling:LTE:CELL:BBGindex \n
		Snippet: value: int = driver.sense.signaling.lte.cell.bbgIndex.get(cell_name = 'abc') \n
		Returns the number of the baseband group containing the cell. Cells in the same group use the same connectors. \n
			:param cell_name: No help available
			:return: bb_group_index: NAV means that the cell is not contained in a baseband group."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:LTE:CELL:BBGindex? {param}')
		return Conversions.str_to_int(response)
