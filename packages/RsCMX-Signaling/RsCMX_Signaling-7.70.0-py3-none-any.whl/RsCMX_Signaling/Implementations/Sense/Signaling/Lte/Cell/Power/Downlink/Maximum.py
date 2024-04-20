from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self, cell_name: str) -> float:
		"""SCPI: SENSe:SIGNaling:LTE:CELL:POWer:DL:MAXimum \n
		Snippet: value: float = driver.sense.signaling.lte.cell.power.downlink.maximum.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: max_cell_power: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:LTE:CELL:POWer:DL:MAXimum? {param}')
		return Conversions.str_to_float(response)
