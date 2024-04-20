from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmsCls:
	"""Sms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sms", core, parent)

	def get_scentre(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:SMS:SCENtre \n
		Snippet: value: str = driver.configure.signaling.sms.get_scentre() \n
		Configures the number of the short message service center used by the originator of the message. \n
			:return: address: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:SMS:SCENtre?')
		return trim_str_response(response)

	def set_scentre(self, address: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:SMS:SCENtre \n
		Snippet: driver.configure.signaling.sms.set_scentre(address = 'abc') \n
		Configures the number of the short message service center used by the originator of the message. \n
			:param address: No help available
		"""
		param = Conversions.value_to_quoted_str(address)
		self._core.io.write(f'CONFigure:SIGNaling:SMS:SCENtre {param}')
