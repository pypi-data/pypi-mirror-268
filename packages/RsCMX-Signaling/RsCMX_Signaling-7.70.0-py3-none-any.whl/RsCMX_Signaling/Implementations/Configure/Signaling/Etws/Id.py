from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdCls:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def set(self, network_scope: str, identifier: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:ID \n
		Snippet: driver.configure.signaling.etws.id.set(network_scope = 'abc', identifier = 1) \n
		Defines the message identifier for ETWS primary notifications. \n
			:param network_scope: No help available
			:param identifier: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('identifier', identifier, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:ETWS:ID {param}'.rstrip())

	def get(self, network_scope: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:ID \n
		Snippet: value: int = driver.configure.signaling.etws.id.get(network_scope = 'abc') \n
		Defines the message identifier for ETWS primary notifications. \n
			:param network_scope: No help available
			:return: identifier: No help available"""
		param = Conversions.value_to_quoted_str(network_scope)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:ETWS:ID? {param}')
		return Conversions.str_to_int(response)
