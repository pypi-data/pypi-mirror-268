from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InstanceCls:
	"""Instance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("instance", core, parent)

	def get(self, cell_name: str) -> str:
		"""SCPI: SENSe:SIGNaling:CELL:INSTance \n
		Snippet: value: str = driver.sense.signaling.cell.instance.get(cell_name = 'abc') \n
		Queries the default cell name corresponding to the current cell name. The command is useful to derive the name of trigger
		signals, see 'Trigger signals'. \n
			:param cell_name: Cell name that is used in most commands and GUI squares.
			:return: cell_instance: Default cell name. Used in names of trigger signals related to the cell."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:CELL:INSTance? {param}')
		return trim_str_response(response)
