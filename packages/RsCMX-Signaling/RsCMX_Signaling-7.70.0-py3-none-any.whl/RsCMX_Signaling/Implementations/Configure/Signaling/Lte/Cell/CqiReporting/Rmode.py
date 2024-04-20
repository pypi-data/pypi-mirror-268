from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmodeCls:
	"""Rmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmode", core, parent)

	def set(self, cell_name: str, report_mode: enums.ReportMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:CQIReporting:RMODe \n
		Snippet: driver.configure.signaling.lte.cell.cqiReporting.rmode.set(cell_name = 'abc', report_mode = enums.ReportMode.S1) \n
		Configures the parameter 'csi-ReportMode', signaled to the UE. \n
			:param cell_name: No help available
			:param report_mode: S1: submode 1 S2: submode 2
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('report_mode', report_mode, DataType.Enum, enums.ReportMode))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:CQIReporting:RMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ReportMode:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:CQIReporting:RMODe \n
		Snippet: value: enums.ReportMode = driver.configure.signaling.lte.cell.cqiReporting.rmode.get(cell_name = 'abc') \n
		Configures the parameter 'csi-ReportMode', signaled to the UE. \n
			:param cell_name: No help available
			:return: report_mode: S1: submode 1 S2: submode 2"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:CQIReporting:RMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ReportMode)
