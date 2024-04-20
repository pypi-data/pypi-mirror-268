from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellsCls:
	"""Cells commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cells", core, parent)

	def get(self, measInstance=repcap.MeasInstance.Default) -> List[str]:
		"""SCPI: CATalog:LTE:MEASurement<Instance>:NETWork:CELLs \n
		Snippet: value: List[str] = driver.catalog.lte.measurement.network.cells.get(measInstance = repcap.MeasInstance.Default) \n
		No command help available \n
			:param measInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Measurement')
			:return: cell_name: No help available"""
		measInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(measInstance, repcap.MeasInstance)
		response = self._core.io.query_str(f'CATalog:LTE:MEASurement{measInstance_cmd_val}:NETWork:CELLs?')
		return Conversions.str_to_str_list(response)
