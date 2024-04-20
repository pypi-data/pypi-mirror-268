from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, cell_group_name: str) -> bool:
		"""SCPI: SENSe:SIGNaling:NRADio:CA:DORMancy:STATe \n
		Snippet: value: bool = driver.sense.signaling.nradio.ca.dormancy.state.get(cell_group_name = 'abc') \n
		Queries the dormancy state of a cell group. \n
			:param cell_group_name: No help available
			:return: dormant_state: Dormant (ON) or non-dormant (OFF) ."""
		param = Conversions.value_to_quoted_str(cell_group_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CA:DORMancy:STATe? {param}')
		return Conversions.str_to_bool(response)
