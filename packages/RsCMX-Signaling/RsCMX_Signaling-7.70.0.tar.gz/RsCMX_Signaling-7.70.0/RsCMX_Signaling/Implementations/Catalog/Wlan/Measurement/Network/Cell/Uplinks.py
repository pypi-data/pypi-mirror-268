from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinksCls:
	"""Uplinks commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplinks", core, parent)

	def get(self, cell_name: str, measInstance=repcap.MeasInstance.Default) -> List[int]:
		"""SCPI: CATalog:WLAN:MEASurement<Instance>:NETWork:CELL:UPLinks \n
		Snippet: value: List[int] = driver.catalog.wlan.measurement.network.cell.uplinks.get(cell_name = 'abc', measInstance = repcap.MeasInstance.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param measInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Measurement')
			:return: available_ul: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		measInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(measInstance, repcap.MeasInstance)
		response = self._core.io.query_bin_or_ascii_int_list(f'CATalog:WLAN:MEASurement{measInstance_cmd_val}:NETWork:CELL:UPLinks? {param}')
		return response
