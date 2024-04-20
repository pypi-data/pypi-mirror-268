from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerCls:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	def get_source(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:TRIGger:SOURce \n
		Snippet: value: List[str] = driver.catalog.signaling.trigger.get_source() \n
		Queries a list of all inactive trigger types that can be activated using method RsCMX_Signaling.Configure.Signaling.
		Trigger.scope. \n
			:return: trigger: Comma-separated list of strings, one string per trigger type.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:TRIGger:SOURce?')
		return Conversions.str_to_str_list(response)
