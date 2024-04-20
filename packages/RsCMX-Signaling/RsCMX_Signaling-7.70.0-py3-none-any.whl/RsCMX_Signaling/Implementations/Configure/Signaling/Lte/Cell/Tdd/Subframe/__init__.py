from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubframeCls:
	"""Subframe commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subframe", core, parent)

	@property
	def assignment(self):
		"""assignment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_assignment'):
			from .Assignment import AssignmentCls
			self._assignment = AssignmentCls(self._core, self._cmd_group)
		return self._assignment

	@property
	def special(self):
		"""special commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_special'):
			from .Special import SpecialCls
			self._special = SpecialCls(self._core, self._cmd_group)
		return self._special

	def set(self, cell_name: str, assignment: enums.Assignment, special_pattern: enums.SpecialPattern = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TDD:SUBFrame \n
		Snippet: driver.configure.signaling.lte.cell.tdd.subframe.set(cell_name = 'abc', assignment = enums.Assignment.NONE, special_pattern = enums.SpecialPattern.P0) \n
		Defines the structure of a TDD radio frame. \n
			:param cell_name: No help available
			:param assignment: Subframe assignment, defining the combination of UL, DL and special subframes.
			:param special_pattern: Inner structure of special subframes.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('assignment', assignment, DataType.Enum, enums.Assignment), ArgSingle('special_pattern', special_pattern, DataType.Enum, enums.SpecialPattern, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:TDD:SUBFrame {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Assignment: enums.Assignment: Subframe assignment, defining the combination of UL, DL and special subframes.
			- Special_Pattern: enums.SpecialPattern: Inner structure of special subframes."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Assignment', enums.Assignment),
			ArgStruct.scalar_enum('Special_Pattern', enums.SpecialPattern)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Assignment: enums.Assignment = None
			self.Special_Pattern: enums.SpecialPattern = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TDD:SUBFrame \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.tdd.subframe.get(cell_name = 'abc') \n
		Defines the structure of a TDD radio frame. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:TDD:SUBFrame? {param}', self.__class__.GetStruct())

	def clone(self) -> 'SubframeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SubframeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
