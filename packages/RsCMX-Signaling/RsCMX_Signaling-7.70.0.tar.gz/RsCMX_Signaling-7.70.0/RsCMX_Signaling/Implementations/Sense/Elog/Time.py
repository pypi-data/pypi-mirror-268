from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeCls:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Severity: List[enums.Severity]: No parameter help available
			- Timestamp: List[str]: No parameter help available
			- Message: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Severity', DataType.EnumList, enums.Severity, False, True, 1),
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Message', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Severity: List[enums.Severity] = None
			self.Timestamp: List[str] = None
			self.Message: List[str] = None

	def get(self, time_start: str, time_end: str) -> GetStruct:
		"""SCPI: SENSe:ELOG:TIME \n
		Snippet: value: GetStruct = driver.sense.elog.time.get(time_start = 'abc', time_end = 'abc') \n
		No command help available \n
			:param time_start: No help available
			:param time_end: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('time_start', time_start, DataType.String), ArgSingle('time_end', time_end, DataType.String))
		return self._core.io.query_struct(f'SENSe:ELOG:TIME? {param}'.rstrip(), self.__class__.GetStruct())
