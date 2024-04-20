from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AuthCls:
	"""Auth commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auth", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:ENABle \n
		Snippet: value: bool = driver.configure.signaling.fgs.nas.auth.get_enable() \n
		Enables authentication for 5GS tracking areas. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:AUTH:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:ENABle \n
		Snippet: driver.configure.signaling.fgs.nas.auth.set_enable(enable = False) \n
		Enables authentication for 5GS tracking areas. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:AUTH:ENABle {param}')

	def get_rand(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:RAND \n
		Snippet: value: str = driver.configure.signaling.fgs.nas.auth.get_rand() \n
		Defines the random number (RAND) to be used for authentication in 5GS tracking areas. \n
			:return: rand: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:AUTH:RAND?')
		return trim_str_response(response)

	def set_rand(self, rand: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:RAND \n
		Snippet: driver.configure.signaling.fgs.nas.auth.set_rand(rand = 'abc') \n
		Defines the random number (RAND) to be used for authentication in 5GS tracking areas. \n
			:param rand: No help available
		"""
		param = Conversions.value_to_quoted_str(rand)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:AUTH:RAND {param}')

	def get_ires(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:IRES \n
		Snippet: value: bool = driver.configure.signaling.fgs.nas.auth.get_ires() \n
		Enables ignoring the RES* in 5GS tracking areas (successful authentication, even if the UE returns a wrong RES* value) . \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:AUTH:IRES?')
		return Conversions.str_to_bool(response)

	def set_ires(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:IRES \n
		Snippet: driver.configure.signaling.fgs.nas.auth.set_ires(enable = False) \n
		Enables ignoring the RES* in 5GS tracking areas (successful authentication, even if the UE returns a wrong RES* value) . \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:AUTH:IRES {param}')
