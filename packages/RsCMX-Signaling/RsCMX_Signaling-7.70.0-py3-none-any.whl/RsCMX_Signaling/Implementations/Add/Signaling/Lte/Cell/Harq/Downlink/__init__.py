from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def rvSequence(self):
		"""rvSequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvSequence'):
			from .RvSequence import RvSequenceCls
			self._rvSequence = RvSequenceCls(self._core, self._cmd_group)
		return self._rvSequence

	# noinspection PyTypeChecker
	class ReTxStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Cell_Name: str: No parameter help available
			- Count: int: Optional setting parameter. Number of entries to be added.
			- Riv: List[enums.Riv]: Optional setting parameter. RIV non-adaptive, new TX RIV
			- Tb_1: List[int]: Optional setting parameter. MCS value for first transport block
			- Tb_2: List[int]: Optional setting parameter. MCS value for second transport block
			- Behavior: List[enums.ReTxBehavior]: Optional setting parameter. Behavior for transport block size changes. Not applicable, flush HARQ buffer, retain HARQ buffer."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int_optional('Count'),
			ArgStruct('Riv', DataType.EnumList, enums.Riv, True, True, 1),
			ArgStruct('Tb_1', DataType.IntegerList, None, True, True, 1),
			ArgStruct('Tb_2', DataType.IntegerList, None, True, True, 1),
			ArgStruct('Behavior', DataType.EnumList, enums.ReTxBehavior, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Count: int = None
			self.Riv: List[enums.Riv] = None
			self.Tb_1: List[int] = None
			self.Tb_2: List[int] = None
			self.Behavior: List[enums.ReTxBehavior] = None

	def set_re_tx(self, value: ReTxStruct) -> None:
		"""SCPI: ADD:SIGNaling:LTE:CELL:HARQ:DL:RETX \n
		Snippet with structure: \n
		structure = driver.add.signaling.lte.cell.harq.downlink.ReTxStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Count: int = 1 \n
		structure.Riv: List[enums.Riv] = [Riv.NADaptive, Riv.NEW] \n
		structure.Tb_1: List[int] = [1, 2, 3] \n
		structure.Tb_2: List[int] = [1, 2, 3] \n
		structure.Behavior: List[enums.ReTxBehavior] = [ReTxBehavior.FLUSh, ReTxBehavior.RETain] \n
		driver.add.signaling.lte.cell.harq.downlink.set_re_tx(value = structure) \n
		Adds entries to the end of the retransmission configuration. \n
			:param value: see the help for ReTxStruct structure arguments.
		"""
		self._core.io.write_struct('ADD:SIGNaling:LTE:CELL:HARQ:DL:RETX', value)

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
