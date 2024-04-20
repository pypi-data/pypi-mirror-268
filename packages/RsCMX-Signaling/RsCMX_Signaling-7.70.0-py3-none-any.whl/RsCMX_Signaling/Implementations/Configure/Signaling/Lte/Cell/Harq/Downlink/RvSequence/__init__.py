from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvSequenceCls:
	"""RvSequence commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvSequence", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	def set(self, cell_name: str, index: List[int], tb_1: List[enums.Version], tb_2: List[enums.Version], qam_64: List[enums.Version]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RVSequence \n
		Snippet: driver.configure.signaling.lte.cell.harq.downlink.rvSequence.set(cell_name = 'abc', index = [1, 2, 3], tb_1 = [Version.AUTO, Version.RV3], tb_2 = [Version.AUTO, Version.RV3], qam_64 = [Version.AUTO, Version.RV3]) \n
		Configures existing entries of user-defined RV sequences. If the mode is not user-defined, it is changed to user-defined.
		A query returns the sequences of the active mode, without changing the mode. \n
			:param cell_name: No help available
			:param index: Index of the entry to be configured (lowest index is 0) .
			:param tb_1: RV sequence for the first transport block, for QPSK and 16QAM.
			:param tb_2: RV sequence for the second transport block, for QPSK and 16QAM.
			:param qam_64: RV sequence for 64QAM and 256QAM, first and second transport block.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle.as_open_list('index', index, DataType.IntegerList, None), ArgSingle.as_open_list('tb_1', tb_1, DataType.EnumList, enums.Version), ArgSingle.as_open_list('tb_2', tb_2, DataType.EnumList, enums.Version), ArgSingle.as_open_list('qam_64', qam_64, DataType.EnumList, enums.Version))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RVSequence {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: List[int]: Index of the entry to be configured (lowest index is 0) .
			- Tb_1: List[enums.Version]: RV sequence for the first transport block, for QPSK and 16QAM.
			- Tb_2: List[enums.Version]: RV sequence for the second transport block, for QPSK and 16QAM.
			- Qam_64: List[enums.Version]: RV sequence for 64QAM and 256QAM, first and second transport block."""
		__meta_args_list = [
			ArgStruct('Index', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tb_1', DataType.EnumList, enums.Version, False, True, 1),
			ArgStruct('Tb_2', DataType.EnumList, enums.Version, False, True, 1),
			ArgStruct('Qam_64', DataType.EnumList, enums.Version, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: List[int] = None
			self.Tb_1: List[enums.Version] = None
			self.Tb_2: List[enums.Version] = None
			self.Qam_64: List[enums.Version] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RVSequence \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.harq.downlink.rvSequence.get(cell_name = 'abc') \n
		Configures existing entries of user-defined RV sequences. If the mode is not user-defined, it is changed to user-defined.
		A query returns the sequences of the active mode, without changing the mode. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RVSequence? {param}', self.__class__.GetStruct())

	def clone(self) -> 'RvSequenceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RvSequenceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
