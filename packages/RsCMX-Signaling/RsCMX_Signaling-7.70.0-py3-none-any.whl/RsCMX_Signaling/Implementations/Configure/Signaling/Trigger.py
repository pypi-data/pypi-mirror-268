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

	def get_scope(self) -> List[str]:
		"""SCPI: CONFigure:SIGNaling:TRIGger:SCOPe \n
		Snippet: value: List[str] = driver.configure.signaling.trigger.get_scope() \n
		Activates one or more trigger types. You can query all inactive trigger types via method RsCMX_Signaling.Catalog.
		Signaling.Trigger.source. \n
			:return: trigger: Comma-separated list of strings, one string per trigger type to be activated.
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TRIGger:SCOPe?')
		return Conversions.str_to_str_list(response)

	def set_scope(self, trigger: List[str]) -> None:
		"""SCPI: CONFigure:SIGNaling:TRIGger:SCOPe \n
		Snippet: driver.configure.signaling.trigger.set_scope(trigger = ['abc1', 'abc2', 'abc3']) \n
		Activates one or more trigger types. You can query all inactive trigger types via method RsCMX_Signaling.Catalog.
		Signaling.Trigger.source. \n
			:param trigger: Comma-separated list of strings, one string per trigger type to be activated.
		"""
		param = Conversions.list_to_csv_quoted_str(trigger)
		self._core.io.write(f'CONFigure:SIGNaling:TRIGger:SCOPe {param}')
