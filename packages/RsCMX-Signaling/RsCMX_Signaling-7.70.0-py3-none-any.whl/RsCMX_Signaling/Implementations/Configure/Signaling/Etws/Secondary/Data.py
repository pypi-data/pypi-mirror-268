from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, network_scope: str, data: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:SECondary:DATA \n
		Snippet: driver.configure.signaling.etws.secondary.data.set(network_scope = 'abc', data = 'abc') \n
		Defines the broadcasted ETWS secondary notification text. \n
			:param network_scope: No help available
			:param data: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('data', data, DataType.String))
		self._core.io.write(f'CONFigure:SIGNaling:ETWS:SECondary:DATA {param}'.rstrip())

	def get(self, network_scope: str) -> str:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:SECondary:DATA \n
		Snippet: value: str = driver.configure.signaling.etws.secondary.data.get(network_scope = 'abc') \n
		Defines the broadcasted ETWS secondary notification text. \n
			:param network_scope: No help available
			:return: data: No help available"""
		param = Conversions.value_to_quoted_str(network_scope)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:ETWS:SECondary:DATA? {param}')
		return trim_str_response(response)
