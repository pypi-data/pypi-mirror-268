from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LanguageCls:
	"""Language commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("language", core, parent)

	def set(self, network_scope: str, language: enums.LanguageB, cgroup_language: enums.GroupLanguage = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:SECondary:LANGuage \n
		Snippet: driver.configure.signaling.etws.secondary.language.set(network_scope = 'abc', language = enums.LanguageB.DANish, cgroup_language = enums.GroupLanguage.G7L) \n
		Selects the language string and sets the coding group for ETWS secondary notifications. \n
			:param network_scope: No help available
			:param language: (enum or string) Two-character language string
			:param cgroup_language: Selects the coding group (GSM 7-bit or UCS-2) . Omitting the value sets G7L.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('language', language, DataType.EnumExt, enums.LanguageB), ArgSingle('cgroup_language', cgroup_language, DataType.Enum, enums.GroupLanguage, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:ETWS:SECondary:LANGuage {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Language: enums.LanguageB: Two-character language string
			- Cgroup_Language: enums.GroupLanguage: Selects the coding group (GSM 7-bit or UCS-2) . Omitting the value sets G7L."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Language', enums.LanguageB),
			ArgStruct.scalar_enum('Cgroup_Language', enums.GroupLanguage)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Language: enums.LanguageB = None
			self.Cgroup_Language: enums.GroupLanguage = None

	def get(self, network_scope: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:ETWS:SECondary:LANGuage \n
		Snippet: value: GetStruct = driver.configure.signaling.etws.secondary.language.get(network_scope = 'abc') \n
		Selects the language string and sets the coding group for ETWS secondary notifications. \n
			:param network_scope: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(network_scope)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:ETWS:SECondary:LANGuage? {param}', self.__class__.GetStruct())
