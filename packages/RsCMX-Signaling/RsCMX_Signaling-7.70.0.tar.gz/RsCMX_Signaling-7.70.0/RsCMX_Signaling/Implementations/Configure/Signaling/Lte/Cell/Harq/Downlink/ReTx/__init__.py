from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReTxCls:
	"""ReTx commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reTx", core, parent)

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def behavior(self):
		"""behavior commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_behavior'):
			from .Behavior import BehaviorCls
			self._behavior = BehaviorCls(self._core, self._cmd_group)
		return self._behavior

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Index: List[int]: Index of the entry to be configured (lowest index is 0) .
			- Riv: List[enums.Riv]: RIV non-adaptive, new TX RIV
			- Tb_1: List[int]: MCS value for first transport block
			- Tb_2: List[int]: MCS value for second transport block
			- Behavior: List[enums.ReTxBehavior]: Behavior for transport block size changes. Not applicable, flush HARQ buffer, retain HARQ buffer."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct('Index', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Riv', DataType.EnumList, enums.Riv, False, True, 1),
			ArgStruct('Tb_1', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tb_2', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Behavior', DataType.EnumList, enums.ReTxBehavior, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Index: List[int] = None
			self.Riv: List[enums.Riv] = None
			self.Tb_1: List[int] = None
			self.Tb_2: List[int] = None
			self.Behavior: List[enums.ReTxBehavior] = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RETX \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.cell.harq.downlink.reTx.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Index: List[int] = [1, 2, 3] \n
		structure.Riv: List[enums.Riv] = [Riv.NADaptive, Riv.NEW] \n
		structure.Tb_1: List[int] = [1, 2, 3] \n
		structure.Tb_2: List[int] = [1, 2, 3] \n
		structure.Behavior: List[enums.ReTxBehavior] = [ReTxBehavior.FLUSh, ReTxBehavior.RETain] \n
		driver.configure.signaling.lte.cell.harq.downlink.reTx.set(structure) \n
		Configures existing entries of the retransmission configuration. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RETX', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: List[int]: Index of the entry to be configured (lowest index is 0) .
			- Riv: List[enums.Riv]: RIV non-adaptive, new TX RIV
			- Tb_1: List[int]: MCS value for first transport block
			- Tb_2: List[int]: MCS value for second transport block
			- Behavior: List[enums.ReTxBehavior]: Behavior for transport block size changes. Not applicable, flush HARQ buffer, retain HARQ buffer."""
		__meta_args_list = [
			ArgStruct('Index', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Riv', DataType.EnumList, enums.Riv, False, True, 1),
			ArgStruct('Tb_1', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tb_2', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Behavior', DataType.EnumList, enums.ReTxBehavior, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: List[int] = None
			self.Riv: List[enums.Riv] = None
			self.Tb_1: List[int] = None
			self.Tb_2: List[int] = None
			self.Behavior: List[enums.ReTxBehavior] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RETX \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.harq.downlink.reTx.get(cell_name = 'abc') \n
		Configures existing entries of the retransmission configuration. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RETX? {param}', self.__class__.GetStruct())

	def clone(self) -> 'ReTxCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReTxCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
