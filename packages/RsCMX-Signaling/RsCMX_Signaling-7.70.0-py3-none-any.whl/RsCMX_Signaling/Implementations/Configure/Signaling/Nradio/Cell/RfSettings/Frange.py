from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrangeCls:
	"""Frange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frange", core, parent)

	def set(self, cell_name: str, frequency_range: enums.FrequencyRange) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:FRANge \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.frange.set(cell_name = 'abc', frequency_range = enums.FrequencyRange.FR1) \n
		Selects the frequency range, FR1 or FR2. \n
			:param cell_name: No help available
			:param frequency_range: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('frequency_range', frequency_range, DataType.Enum, enums.FrequencyRange))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:FRANge {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FrequencyRange:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:FRANge \n
		Snippet: value: enums.FrequencyRange = driver.configure.signaling.nradio.cell.rfSettings.frange.get(cell_name = 'abc') \n
		Selects the frequency range, FR1 or FR2. \n
			:param cell_name: No help available
			:return: frequency_range: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:FRANge? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FrequencyRange)
