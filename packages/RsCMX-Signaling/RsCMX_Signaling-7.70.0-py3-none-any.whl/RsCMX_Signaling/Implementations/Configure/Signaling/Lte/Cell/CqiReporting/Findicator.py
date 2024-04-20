from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FindicatorCls:
	"""Findicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("findicator", core, parent)

	def set(self, cell_name: str, format_py: enums.FormatCqi) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:CQIReporting:FINDicator \n
		Snippet: driver.configure.signaling.lte.cell.cqiReporting.findicator.set(cell_name = 'abc', format_py = enums.FormatCqi.SB) \n
		Configures the parameter 'cqi-FormatIndicatorPeriodic', signaled to the UE. \n
			:param cell_name: No help available
			:param format_py: WB: wideband CQI reporting SB: subband CQI reporting
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('format_py', format_py, DataType.Enum, enums.FormatCqi))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:CQIReporting:FINDicator {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FormatCqi:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:CQIReporting:FINDicator \n
		Snippet: value: enums.FormatCqi = driver.configure.signaling.lte.cell.cqiReporting.findicator.get(cell_name = 'abc') \n
		Configures the parameter 'cqi-FormatIndicatorPeriodic', signaled to the UE. \n
			:param cell_name: No help available
			:return: format_py: WB: wideband CQI reporting SB: subband CQI reporting"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:CQIReporting:FINDicator? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FormatCqi)
