from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReportCls:
	"""UeReport commands group definition. 10 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueReport", core, parent)

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def ncell(self):
		"""ncell commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ncell'):
			from .Ncell import NcellCls
			self._ncell = NcellCls(self._core, self._cmd_group)
		return self._ncell

	# noinspection PyTypeChecker
	def get_enable(self) -> enums.CellsToMeasure:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:ENABle \n
		Snippet: value: enums.CellsToMeasure = driver.configure.signaling.measurement.ueReport.get_enable() \n
		Selects whether the UE must send measurement reports and for which type of serving cell. \n
			:return: cells_to_measure: OFF: no serving cell measurement reports ALL: reporting for any serving cell LTE: reporting for LTE serving cell NRADio: reporting for NR serving cell
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:ENABle?')
		return Conversions.str_to_scalar_enum(response, enums.CellsToMeasure)

	def set_enable(self, cells_to_measure: enums.CellsToMeasure) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:ENABle \n
		Snippet: driver.configure.signaling.measurement.ueReport.set_enable(cells_to_measure = enums.CellsToMeasure.ALL) \n
		Selects whether the UE must send measurement reports and for which type of serving cell. \n
			:param cells_to_measure: OFF: no serving cell measurement reports ALL: reporting for any serving cell LTE: reporting for LTE serving cell NRADio: reporting for NR serving cell
		"""
		param = Conversions.enum_scalar_to_str(cells_to_measure, enums.CellsToMeasure)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:ENABle {param}')

	# noinspection PyTypeChecker
	def get_rinterval(self) -> enums.ReportInterval:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:RINTerval \n
		Snippet: value: enums.ReportInterval = driver.configure.signaling.measurement.ueReport.get_rinterval() \n
		Configures the interval between two consecutive serving cell measurement reports. \n
			:return: report_interval: I1 to I5: 120 ms, 240 ms, 480 ms, 640 ms, 1024 ms I6 to I10: 2048 ms, 5120 ms, 10240 ms, 20480 ms, 40960 ms I11 to I14: 1 min, 6 min, 12 min, 30 min
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:RINTerval?')
		return Conversions.str_to_scalar_enum(response, enums.ReportInterval)

	def set_rinterval(self, report_interval: enums.ReportInterval) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:RINTerval \n
		Snippet: driver.configure.signaling.measurement.ueReport.set_rinterval(report_interval = enums.ReportInterval.I1) \n
		Configures the interval between two consecutive serving cell measurement reports. \n
			:param report_interval: I1 to I5: 120 ms, 240 ms, 480 ms, 640 ms, 1024 ms I6 to I10: 2048 ms, 5120 ms, 10240 ms, 20480 ms, 40960 ms I11 to I14: 1 min, 6 min, 12 min, 30 min
		"""
		param = Conversions.enum_scalar_to_str(report_interval, enums.ReportInterval)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:RINTerval {param}')

	def clone(self) -> 'UeReportCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeReportCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
