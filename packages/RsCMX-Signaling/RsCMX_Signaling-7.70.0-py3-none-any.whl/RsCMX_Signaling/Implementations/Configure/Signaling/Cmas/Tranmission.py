from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TranmissionCls:
	"""Tranmission commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tranmission", core, parent)

	def set(self, network_scope: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:TRANmission \n
		Snippet: driver.configure.signaling.cmas.tranmission.set(network_scope = 'abc', enable = False) \n
		Enables or disables the transmission of CMAS messages via the SIB. \n
			:param network_scope: No help available
			:param enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:CMAS:TRANmission {param}'.rstrip())

	def get(self, network_scope: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:TRANmission \n
		Snippet: value: bool = driver.configure.signaling.cmas.tranmission.get(network_scope = 'abc') \n
		Enables or disables the transmission of CMAS messages via the SIB. \n
			:param network_scope: No help available
			:return: enable: No help available"""
		param = Conversions.value_to_quoted_str(network_scope)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:CMAS:TRANmission? {param}')
		return Conversions.str_to_bool(response)
