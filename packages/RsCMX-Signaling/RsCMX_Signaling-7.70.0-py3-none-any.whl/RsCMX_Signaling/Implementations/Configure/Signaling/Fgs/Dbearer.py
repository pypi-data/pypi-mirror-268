from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DbearerCls:
	"""Dbearer commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbearer", core, parent)

	def get_dn_name(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:FGS:DBEarer:DNName \n
		Snippet: value: str = driver.configure.signaling.fgs.dbearer.get_dn_name() \n
		Configures the default data network name (DNN) for default flows in 5GS tracking areas. \n
			:return: network_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:DBEarer:DNName?')
		return trim_str_response(response)

	def set_dn_name(self, network_name: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:DBEarer:DNName \n
		Snippet: driver.configure.signaling.fgs.dbearer.set_dn_name(network_name = 'abc') \n
		Configures the default data network name (DNN) for default flows in 5GS tracking areas. \n
			:param network_name: No help available
		"""
		param = Conversions.value_to_quoted_str(network_name)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:DBEarer:DNName {param}')

	# noinspection PyTypeChecker
	def get_rlc_mode(self) -> enums.RlcMode:
		"""SCPI: [CONFigure]:SIGNaling:FGS:DBEarer:RLCMode \n
		Snippet: value: enums.RlcMode = driver.configure.signaling.fgs.dbearer.get_rlc_mode() \n
		Configures the RLC mode for default flows in 5GS tracking areas. \n
			:return: rlc_mode: RLC mode ACK: acknowledged UACK: unacknowledged
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:DBEarer:RLCMode?')
		return Conversions.str_to_scalar_enum(response, enums.RlcMode)

	def set_rlc_mode(self, rlc_mode: enums.RlcMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:DBEarer:RLCMode \n
		Snippet: driver.configure.signaling.fgs.dbearer.set_rlc_mode(rlc_mode = enums.RlcMode.ACK) \n
		Configures the RLC mode for default flows in 5GS tracking areas. \n
			:param rlc_mode: RLC mode ACK: acknowledged UACK: unacknowledged
		"""
		param = Conversions.enum_scalar_to_str(rlc_mode, enums.RlcMode)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:DBEarer:RLCMode {param}')
