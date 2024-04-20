from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CqiCls:
	"""Cqi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqi", core, parent)

	def set(self, cell_name: str, report_format: enums.ReportCqi, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:REPort:CQI \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.cqiReporting.report.cqi.set(cell_name = 'abc', report_format = enums.ReportCqi.OFF, bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param report_format: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('report_format', report_format, DataType.Enum, enums.ReportCqi))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:REPort:CQI {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.ReportCqi:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:REPort:CQI \n
		Snippet: value: enums.ReportCqi = driver.configure.signaling.nradio.cell.bwp.cqiReporting.report.cqi.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: report_format: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:REPort:CQI? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ReportCqi)
