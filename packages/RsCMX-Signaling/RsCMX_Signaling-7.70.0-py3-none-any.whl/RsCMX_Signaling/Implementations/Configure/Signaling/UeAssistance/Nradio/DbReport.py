from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DbReportCls:
	"""DbReport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbReport", core, parent)

	def set(self, enable: bool, prohibit_timer: enums.ProhibitTimer = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:DBReport \n
		Snippet: driver.configure.signaling.ueAssistance.nradio.dbReport.set(enable = False, prohibit_timer = enums.ProhibitTimer.INF) \n
		Configures requests for delay budget reports. \n
			:param enable: Enables/disables transmitting the parameter 'delayBudgetReportingConfig' in the IE 'OtherConfig'.
			:param prohibit_timer: Signaled 'delayBudgetReportingProhibitTimer'. Sn: n ms SnDm: n.m ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('prohibit_timer', prohibit_timer, DataType.Enum, enums.ProhibitTimer, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:UEASsistance:NRADio:DBReport {param}'.rstrip())

	# noinspection PyTypeChecker
	class DbReportStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables/disables transmitting the parameter 'delayBudgetReportingConfig' in the IE 'OtherConfig'.
			- Prohibit_Timer: enums.ProhibitTimer: Signaled 'delayBudgetReportingProhibitTimer'. Sn: n ms SnDm: n.m ms"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Prohibit_Timer', enums.ProhibitTimer)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Prohibit_Timer: enums.ProhibitTimer = None

	def get(self) -> DbReportStruct:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:DBReport \n
		Snippet: value: DbReportStruct = driver.configure.signaling.ueAssistance.nradio.dbReport.get() \n
		Configures requests for delay budget reports. \n
			:return: structure: for return value, see the help for DbReportStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:UEASsistance:NRADio:DBReport?', self.__class__.DbReportStruct())
