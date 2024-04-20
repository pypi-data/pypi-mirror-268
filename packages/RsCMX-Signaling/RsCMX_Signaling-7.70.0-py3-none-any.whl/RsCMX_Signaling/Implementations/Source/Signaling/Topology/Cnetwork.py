from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CnetworkCls:
	"""Cnetwork commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnetwork", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: SOURce:SIGNaling:TOPology:CNETwork:ENABle \n
		Snippet: value: bool = driver.source.signaling.topology.cnetwork.get_enable() \n
		Switches between edit mode and live mode. \n
			:return: enable: ON: Switch to live mode. OFF: Switch to edit mode.
		"""
		response = self._core.io.query_str('SOURce:SIGNaling:TOPology:CNETwork:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: SOURce:SIGNaling:TOPology:CNETwork:ENABle \n
		Snippet: driver.source.signaling.topology.cnetwork.set_enable(enable = False) \n
		Switches between edit mode and live mode. \n
			:param enable: ON: Switch to live mode. OFF: Switch to edit mode.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'SOURce:SIGNaling:TOPology:CNETwork:ENABle {param}')
