from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsOffsetCls:
	"""MsOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msOffset", core, parent)

	def set(self, enable: bool, prohibit_timer: enums.ProhibitTimer = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:MSOFfset \n
		Snippet: driver.configure.signaling.ueAssistance.nradio.msOffset.set(enable = False, prohibit_timer = enums.ProhibitTimer.INF) \n
		Configures requests for the preferred minimum scheduling offset. \n
			:param enable: Enables/disables transmitting the parameter 'MinSchedulingOffsetPreferenceConfig-r16' in the IE 'OtherConfig'.
			:param prohibit_timer: Signaled 'minSchedulingOffsetPreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('prohibit_timer', prohibit_timer, DataType.Enum, enums.ProhibitTimer, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:UEASsistance:NRADio:MSOFfset {param}'.rstrip())

	# noinspection PyTypeChecker
	class MsOffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables/disables transmitting the parameter 'MinSchedulingOffsetPreferenceConfig-r16' in the IE 'OtherConfig'.
			- Prohibit_Timer: enums.ProhibitTimer: Signaled 'minSchedulingOffsetPreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Prohibit_Timer', enums.ProhibitTimer)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Prohibit_Timer: enums.ProhibitTimer = None

	def get(self) -> MsOffsetStruct:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:MSOFfset \n
		Snippet: value: MsOffsetStruct = driver.configure.signaling.ueAssistance.nradio.msOffset.get() \n
		Configures requests for the preferred minimum scheduling offset. \n
			:return: structure: for return value, see the help for MsOffsetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:UEASsistance:NRADio:MSOFfset?', self.__class__.MsOffsetStruct())
