from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwpCls:
	"""Bwp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwp", core, parent)

	def get(self, cell_name: str) -> List[int]:
		"""SCPI: CATalog:SIGNaling:NRADio:CELL:BWP \n
		Snippet: value: List[int] = driver.catalog.signaling.nradio.cell.bwp.get(cell_name = 'abc') \n
		Queries a list of all bandwidth parts. \n
			:param cell_name: No help available
			:return: idn: Comma-separated list of BWP IDs, one ID per BWP. The initial BWP has the ID 0. Additional BWPs have the IDs 1 to n."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_bin_or_ascii_int_list(f'CATalog:SIGNaling:NRADio:CELL:BWP? {param}')
		return response
