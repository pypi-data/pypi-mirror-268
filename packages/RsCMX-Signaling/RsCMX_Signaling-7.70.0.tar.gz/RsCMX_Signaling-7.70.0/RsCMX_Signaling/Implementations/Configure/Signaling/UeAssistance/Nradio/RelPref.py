from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelPrefCls:
	"""RelPref commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relPref", core, parent)

	def set(self, enable: bool, prohibit_timer: enums.ProhibitTimer = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:RELPref \n
		Snippet: driver.configure.signaling.ueAssistance.nradio.relPref.set(enable = False, prohibit_timer = enums.ProhibitTimer.INF) \n
		Configures requests for connection release preference information. \n
			:param enable: Enables/disables transmitting the parameter 'ReleasePreferenceConfig-r16' in the IE 'OtherConfig'.
			:param prohibit_timer: Signaled 'releasePreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('prohibit_timer', prohibit_timer, DataType.Enum, enums.ProhibitTimer, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:UEASsistance:NRADio:RELPref {param}'.rstrip())

	# noinspection PyTypeChecker
	class RelPrefStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables/disables transmitting the parameter 'ReleasePreferenceConfig-r16' in the IE 'OtherConfig'.
			- Prohibit_Timer: enums.ProhibitTimer: Signaled 'releasePreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Prohibit_Timer', enums.ProhibitTimer)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Prohibit_Timer: enums.ProhibitTimer = None

	def get(self) -> RelPrefStruct:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:RELPref \n
		Snippet: value: RelPrefStruct = driver.configure.signaling.ueAssistance.nradio.relPref.get() \n
		Configures requests for connection release preference information. \n
			:return: structure: for return value, see the help for RelPrefStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:UEASsistance:NRADio:RELPref?', self.__class__.RelPrefStruct())
