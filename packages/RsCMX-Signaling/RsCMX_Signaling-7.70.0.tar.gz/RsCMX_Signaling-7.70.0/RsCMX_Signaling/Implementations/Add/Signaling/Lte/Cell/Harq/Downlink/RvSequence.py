from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvSequenceCls:
	"""RvSequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvSequence", core, parent)

	def set(self, cell_name: str, count: int = None, tb_1: List[enums.Version] = None, tb_2: List[enums.Version] = None, qam_64: List[enums.Version] = None) -> None:
		"""SCPI: ADD:SIGNaling:LTE:CELL:HARQ:DL:RVSequence \n
		Snippet: driver.add.signaling.lte.cell.harq.downlink.rvSequence.set(cell_name = 'abc', count = 1, tb_1 = [Version.AUTO, Version.RV3], tb_2 = [Version.AUTO, Version.RV3], qam_64 = [Version.AUTO, Version.RV3]) \n
		Adds entries to the end of the RV sequences. \n
			:param cell_name: No help available
			:param count: Number of entries to be added.
			:param tb_1: RV sequence for the first transport block, for QPSK and 16QAM.
			:param tb_2: RV sequence for the second transport block, for QPSK and 16QAM.
			:param qam_64: RV sequence for 64QAM and 256QAM, first and second transport block.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('count', count, DataType.Integer, None, is_optional=True), ArgSingle('tb_1', tb_1, DataType.EnumList, enums.Version, True, True, 1), ArgSingle('tb_2', tb_2, DataType.EnumList, enums.Version, True, True, 1), ArgSingle('qam_64', qam_64, DataType.EnumList, enums.Version, True, True, 1))
		self._core.io.write(f'ADD:SIGNaling:LTE:CELL:HARQ:DL:RVSequence {param}'.rstrip())
