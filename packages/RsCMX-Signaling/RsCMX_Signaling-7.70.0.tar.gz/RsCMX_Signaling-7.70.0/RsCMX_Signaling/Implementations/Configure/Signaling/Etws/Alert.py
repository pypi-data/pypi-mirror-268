from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlertCls:
	"""Alert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alert", core, parent)

	def set(self, network_scope: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:ALERt \n
		Snippet: driver.configure.signaling.etws.alert.set(network_scope = 'abc', enable = False) \n
		Enables an emergency user alert at the UE, for ETWS primary notifications. \n
			:param network_scope: No help available
			:param enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:ETWS:ALERt {param}'.rstrip())

	def get(self, network_scope: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:ALERt \n
		Snippet: value: bool = driver.configure.signaling.etws.alert.get(network_scope = 'abc') \n
		Enables an emergency user alert at the UE, for ETWS primary notifications. \n
			:param network_scope: No help available
			:return: enable: No help available"""
		param = Conversions.value_to_quoted_str(network_scope)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:ETWS:ALERt? {param}')
		return Conversions.str_to_bool(response)
