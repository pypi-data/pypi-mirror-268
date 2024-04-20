from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsReportCls:
	"""SsReport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssReport", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:SSReport:ENABle \n
		Snippet: value: bool = driver.configure.signaling.tmode.ssReport.get_enable() \n
		Enables SS-RSRPB reporting by the UE. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:TMODe:SSReport:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:SSReport:ENABle \n
		Snippet: driver.configure.signaling.tmode.ssReport.set_enable(enable = False) \n
		Enables SS-RSRPB reporting by the UE. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:TMODe:SSReport:ENABle {param}')
