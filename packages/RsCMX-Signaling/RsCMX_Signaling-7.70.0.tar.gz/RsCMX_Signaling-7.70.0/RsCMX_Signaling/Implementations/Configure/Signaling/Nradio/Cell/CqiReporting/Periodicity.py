from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, cell_name: str, periodicity: enums.PeriodicityCqiReport) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:PERiodicity \n
		Snippet: driver.configure.signaling.nradio.cell.cqiReporting.periodicity.set(cell_name = 'abc', periodicity = enums.PeriodicityCqiReport.P10) \n
		Selects the global periodicity for CSI reporting and CSI-RS resources. \n
			:param cell_name: No help available
			:param periodicity: Periodicity in slots
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Enum, enums.PeriodicityCqiReport))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:PERiodicity {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PeriodicityCqiReport:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:PERiodicity \n
		Snippet: value: enums.PeriodicityCqiReport = driver.configure.signaling.nradio.cell.cqiReporting.periodicity.get(cell_name = 'abc') \n
		Selects the global periodicity for CSI reporting and CSI-RS resources. \n
			:param cell_name: No help available
			:return: periodicity: Periodicity in slots"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:PERiodicity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PeriodicityCqiReport)
