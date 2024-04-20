from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def set(self, cell_name: str, used_ul: List[int] = None, measInstance=repcap.MeasInstance.Default) -> None:
		"""SCPI: [CONFigure]:NRSub:MEASurement<Instance>:NETWork:CELL \n
		Snippet: driver.configure.nrSub.measurement.network.cell.set(cell_name = 'abc', used_ul = [1, 2, 3], measInstance = repcap.MeasInstance.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param used_ul: No help available
			:param measInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Measurement')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('used_ul', used_ul, DataType.IntegerList, None, True, True, 1))
		measInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(measInstance, repcap.MeasInstance)
		self._core.io.write(f'CONFigure:NRSub:MEASurement{measInstance_cmd_val}:NETWork:CELL {param}'.rstrip())

	# noinspection PyTypeChecker
	class CellStruct(StructBase):
		"""Response structure. Fields: \n
			- Cell_Name: str: No parameter help available
			- Used_Ul: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct('Used_Ul', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Used_Ul: List[int] = None

	def get(self, measInstance=repcap.MeasInstance.Default) -> CellStruct:
		"""SCPI: [CONFigure]:NRSub:MEASurement<Instance>:NETWork:CELL \n
		Snippet: value: CellStruct = driver.configure.nrSub.measurement.network.cell.get(measInstance = repcap.MeasInstance.Default) \n
		No command help available \n
			:param measInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Measurement')
			:return: structure: for return value, see the help for CellStruct structure arguments."""
		measInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(measInstance, repcap.MeasInstance)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement{measInstance_cmd_val}:NETWork:CELL?', self.__class__.CellStruct())
