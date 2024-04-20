from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConnectionCls:
	"""Connection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	# noinspection PyTypeChecker
	class UePowerStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Status: enums.PowerStatus: No parameter help available
			- Power_Level: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Status', enums.PowerStatus),
			ArgStruct('Power_Level', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Status: enums.PowerStatus = None
			self.Power_Level: List[float] = None

	def get_ue_power(self) -> UePowerStruct:
		"""SCPI: SENSe:SIGNaling:UE:CONNection:UEPower \n
		Snippet: value: UePowerStruct = driver.sense.signaling.ue.connection.get_ue_power() \n
		No command help available \n
			:return: structure: for return value, see the help for UePowerStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:SIGNaling:UE:CONNection:UEPower?', self.__class__.UePowerStruct())
