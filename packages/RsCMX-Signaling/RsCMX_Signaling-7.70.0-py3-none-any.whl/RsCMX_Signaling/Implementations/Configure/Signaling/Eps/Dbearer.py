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

	def get_apn(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:EPS:DBEarer:APN \n
		Snippet: value: str = driver.configure.signaling.eps.dbearer.get_apn() \n
		Configures the default APN for default bearers in EPS tracking areas. \n
			:return: apn: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:DBEarer:APN?')
		return trim_str_response(response)

	def set_apn(self, apn: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:DBEarer:APN \n
		Snippet: driver.configure.signaling.eps.dbearer.set_apn(apn = 'abc') \n
		Configures the default APN for default bearers in EPS tracking areas. \n
			:param apn: No help available
		"""
		param = Conversions.value_to_quoted_str(apn)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:DBEarer:APN {param}')

	# noinspection PyTypeChecker
	def get_rlc_mode(self) -> enums.RlcMode:
		"""SCPI: [CONFigure]:SIGNaling:EPS:DBEarer:RLCMode \n
		Snippet: value: enums.RlcMode = driver.configure.signaling.eps.dbearer.get_rlc_mode() \n
		Configures the RLC mode for default bearers in EPS tracking areas. \n
			:return: rlc_mode: RLC mode ACK: acknowledged UACK: unacknowledged
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:DBEarer:RLCMode?')
		return Conversions.str_to_scalar_enum(response, enums.RlcMode)

	def set_rlc_mode(self, rlc_mode: enums.RlcMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:DBEarer:RLCMode \n
		Snippet: driver.configure.signaling.eps.dbearer.set_rlc_mode(rlc_mode = enums.RlcMode.ACK) \n
		Configures the RLC mode for default bearers in EPS tracking areas. \n
			:param rlc_mode: RLC mode ACK: acknowledged UACK: unacknowledged
		"""
		param = Conversions.enum_scalar_to_str(rlc_mode, enums.RlcMode)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:DBEarer:RLCMode {param}')
