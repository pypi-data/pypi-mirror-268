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
class LastCls:
	"""Last commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("last", core, parent)

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

	def get(self, count: int = None) -> GetStruct:
		"""SCPI: SENSe:ELOG:LAST \n
		Snippet: value: GetStruct = driver.sense.elog.last.get(count = 1) \n
		No command help available \n
			:param count: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('count', count, DataType.Integer, None, is_optional=True))
		return self._core.io.query_struct(f'SENSe:ELOG:LAST? {param}'.rstrip(), self.__class__.GetStruct())
