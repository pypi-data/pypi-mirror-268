from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcellCls:
	"""Ncell commands group definition. 7 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncell", core, parent)

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	def get_enable(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:ENABle \n
		Snippet: value: bool = driver.configure.signaling.measurement.ueReport.ncell.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:NCELl:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:ENABle \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.set_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:ENABle {param}')

	# noinspection PyTypeChecker
	def get_rinterval(self) -> enums.ReportInterval:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RINTerval \n
		Snippet: value: enums.ReportInterval = driver.configure.signaling.measurement.ueReport.ncell.get_rinterval() \n
		Configures the interval between two consecutive neighbor cell measurement reports. Applies only to <Type> = CNETwork, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
			:return: report_interval: I1 to I5: 120 ms, 240 ms, 480 ms, 640 ms, 1024 ms I6 to I10: 2048 ms, 5120 ms, 10240 ms, 20480 ms, 40960 ms I11 to I14: 1 min, 6 min, 12 min, 30 min
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RINTerval?')
		return Conversions.str_to_scalar_enum(response, enums.ReportInterval)

	def set_rinterval(self, report_interval: enums.ReportInterval) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RINTerval \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.set_rinterval(report_interval = enums.ReportInterval.I1) \n
		Configures the interval between two consecutive neighbor cell measurement reports. Applies only to <Type> = CNETwork, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
			:param report_interval: I1 to I5: 120 ms, 240 ms, 480 ms, 640 ms, 1024 ms I6 to I10: 2048 ms, 5120 ms, 10240 ms, 20480 ms, 40960 ms I11 to I14: 1 min, 6 min, 12 min, 30 min
		"""
		param = Conversions.enum_scalar_to_str(report_interval, enums.ReportInterval)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RINTerval {param}')

	def clone(self) -> 'NcellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NcellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
