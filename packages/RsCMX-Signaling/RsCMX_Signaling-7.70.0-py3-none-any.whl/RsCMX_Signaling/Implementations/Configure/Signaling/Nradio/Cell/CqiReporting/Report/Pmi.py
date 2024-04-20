from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmiCls:
	"""Pmi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmi", core, parent)

	def set(self, cell_name: str, report_format: enums.ReportCqi) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:REPort:PMI \n
		Snippet: driver.configure.signaling.nradio.cell.cqiReporting.report.pmi.set(cell_name = 'abc', report_format = enums.ReportCqi.OFF) \n
		Configures the parameter 'pmi-FormatIndicator' signaled to the UE. \n
			:param cell_name: No help available
			:param report_format: OFF: no PMI reporting WB: wideband PMI reporting SB: subband PMI reporting
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('report_format', report_format, DataType.Enum, enums.ReportCqi))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:REPort:PMI {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ReportCqi:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:REPort:PMI \n
		Snippet: value: enums.ReportCqi = driver.configure.signaling.nradio.cell.cqiReporting.report.pmi.get(cell_name = 'abc') \n
		Configures the parameter 'pmi-FormatIndicator' signaled to the UE. \n
			:param cell_name: No help available
			:return: report_format: OFF: no PMI reporting WB: wideband PMI reporting SB: subband PMI reporting"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:REPort:PMI? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ReportCqi)
