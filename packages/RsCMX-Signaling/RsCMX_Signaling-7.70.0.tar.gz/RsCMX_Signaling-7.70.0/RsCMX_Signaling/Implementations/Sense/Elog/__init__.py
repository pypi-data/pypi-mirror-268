from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ElogCls:
	"""Elog commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("elog", core, parent)

	@property
	def last(self):
		"""last commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_last'):
			from .Last import LastCls
			self._last = LastCls(self._core, self._cmd_group)
		return self._last

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	# noinspection PyTypeChecker
	class AllStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
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

	def get_all(self) -> AllStruct:
		"""SCPI: SENSe:ELOG:ALL \n
		Snippet: value: AllStruct = driver.sense.elog.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:ELOG:ALL?', self.__class__.AllStruct())

	def clone(self) -> 'ElogCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ElogCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
