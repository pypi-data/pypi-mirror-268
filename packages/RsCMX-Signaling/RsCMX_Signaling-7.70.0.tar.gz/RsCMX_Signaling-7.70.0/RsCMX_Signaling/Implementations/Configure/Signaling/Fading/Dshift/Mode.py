from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.FadingMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FADing:DSHift:MODE \n
		Snippet: driver.configure.signaling.fading.dshift.mode.set(cell_name = 'abc', mode = enums.FadingMode.NORMal) \n
		Selects the Doppler shift mode for fading. \n
			:param cell_name: No help available
			:param mode: NORMal: The maximum Doppler frequency is determined by the fading profile. USER: The maximum Doppler frequency is configurable.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.FadingMode))
		self._core.io.write(f'CONFigure:SIGNaling:FADing:DSHift:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FadingMode:
		"""SCPI: [CONFigure]:SIGNaling:FADing:DSHift:MODE \n
		Snippet: value: enums.FadingMode = driver.configure.signaling.fading.dshift.mode.get(cell_name = 'abc') \n
		Selects the Doppler shift mode for fading. \n
			:param cell_name: No help available
			:return: mode: NORMal: The maximum Doppler frequency is determined by the fading profile. USER: The maximum Doppler frequency is configurable."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:FADing:DSHift:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FadingMode)
