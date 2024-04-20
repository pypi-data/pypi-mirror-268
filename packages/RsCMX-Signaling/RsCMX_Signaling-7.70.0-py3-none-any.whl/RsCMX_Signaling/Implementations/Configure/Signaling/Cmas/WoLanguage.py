from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WoLanguageCls:
	"""WoLanguage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("woLanguage", core, parent)

	def set(self, network_scope: str, language: enums.LanguageB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:WOLanguage \n
		Snippet: driver.configure.signaling.cmas.woLanguage.set(network_scope = 'abc', language = enums.LanguageB.DANish) \n
		Selects the language and sets the coding group 'GSM 7-bit coding without language string', for CMAS messages. \n
			:param network_scope: No help available
			:param language: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('language', language, DataType.Enum, enums.LanguageB))
		self._core.io.write(f'CONFigure:SIGNaling:CMAS:WOLanguage {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, network_scope: str) -> enums.LanguageB:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:WOLanguage \n
		Snippet: value: enums.LanguageB = driver.configure.signaling.cmas.woLanguage.get(network_scope = 'abc') \n
		Selects the language and sets the coding group 'GSM 7-bit coding without language string', for CMAS messages. \n
			:param network_scope: No help available
			:return: language: No help available"""
		param = Conversions.value_to_quoted_str(network_scope)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:CMAS:WOLanguage? {param}')
		return Conversions.str_to_scalar_enum(response, enums.LanguageB)
