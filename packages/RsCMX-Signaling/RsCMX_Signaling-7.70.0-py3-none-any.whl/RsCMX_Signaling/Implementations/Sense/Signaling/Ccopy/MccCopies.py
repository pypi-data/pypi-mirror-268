from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MccCopiesCls:
	"""MccCopies commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mccCopies", core, parent)

	def get(self, cell_name: str) -> int:
		"""SCPI: SENSe:SIGNaling:CCOPy:MCCCopies \n
		Snippet: value: int = driver.sense.signaling.ccopy.mccCopies.get(cell_name = 'abc') \n
		Queries the maximum number of contiguous cell copies for a specific source cell. \n
			:param cell_name: No help available
			:return: no_copies: Number of cells that fit into the same frequency band above the source cell (higher frequencies) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:CCOPy:MCCCopies? {param}')
		return Conversions.str_to_int(response)
