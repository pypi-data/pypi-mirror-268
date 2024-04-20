from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProfileCls:
	"""Profile commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profile", core, parent)

	def set(self, cell_name: str, profile: enums.FadingProfile) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FADing:PROFile \n
		Snippet: driver.configure.signaling.fading.profile.set(cell_name = 'abc', profile = enums.FadingProfile.CTES) \n
		Selects a propagation condition profile for fading. \n
			:param cell_name: No help available
			:param profile: NONE and values listed in Table 'Profile values'
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('profile', profile, DataType.Enum, enums.FadingProfile))
		self._core.io.write(f'CONFigure:SIGNaling:FADing:PROFile {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FadingProfile:
		"""SCPI: [CONFigure]:SIGNaling:FADing:PROFile \n
		Snippet: value: enums.FadingProfile = driver.configure.signaling.fading.profile.get(cell_name = 'abc') \n
		Selects a propagation condition profile for fading. \n
			:param cell_name: No help available
			:return: profile: NONE and values listed in Table 'Profile values'"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:FADing:PROFile? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FadingProfile)
