from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MmLayerCls:
	"""MmLayer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmLayer", core, parent)

	def set(self, enable: bool, prohibit_timer: enums.ProhibitTimer = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:MMLayer \n
		Snippet: driver.configure.signaling.ueAssistance.nradio.mmLayer.set(enable = False, prohibit_timer = enums.ProhibitTimer.INF) \n
		Configures requests for the preferred maximum number of MIMO layers. \n
			:param enable: Enables/disables transmitting the parameter 'MaxMIMO-LayerPreferenceConfig-r16' in the IE 'OtherConfig'.
			:param prohibit_timer: Signaled 'maxMIMO-LayerPreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('prohibit_timer', prohibit_timer, DataType.Enum, enums.ProhibitTimer, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:UEASsistance:NRADio:MMLayer {param}'.rstrip())

	# noinspection PyTypeChecker
	class MmLayerStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables/disables transmitting the parameter 'MaxMIMO-LayerPreferenceConfig-r16' in the IE 'OtherConfig'.
			- Prohibit_Timer: enums.ProhibitTimer: Signaled 'maxMIMO-LayerPreferenceProhibitTimer-r16'. Sn: n ms SnDm: n.m ms"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Prohibit_Timer', enums.ProhibitTimer)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Prohibit_Timer: enums.ProhibitTimer = None

	def get(self) -> MmLayerStruct:
		"""SCPI: [CONFigure]:SIGNaling:UEASsistance:NRADio:MMLayer \n
		Snippet: value: MmLayerStruct = driver.configure.signaling.ueAssistance.nradio.mmLayer.get() \n
		Configures requests for the preferred maximum number of MIMO layers. \n
			:return: structure: for return value, see the help for MmLayerStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:UEASsistance:NRADio:MMLayer?', self.__class__.MmLayerStruct())
