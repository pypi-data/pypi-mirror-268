from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, cell_name: str, enable: List[bool], number_rb: List[int], start_rb: List[int], mcs: List[int]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:ALL \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.all.set(cell_name = 'abc', enable = [True, False, True], number_rb = [1, 2, 3], start_rb = [1, 2, 3], mcs = [1, 2, 3]) \n
		Defines the scheduled RB allocation and the MCS index for all DL subframes. The parameters are entered 10 times, so that
		all subframes are configured by a single command (index = subframe number 0 to 9) : <CellName>, <Enable>0, ..., <Enable>9,
		<NumberRB>0, ..., <NumberRB>9, <StartRB>0, ..., <StartRB>9, <MCS>0, ..., <MCS>9 \n
			:param cell_name: No help available
			:param enable: No help available
			:param number_rb: No help available
			:param start_rb: No help available
			:param mcs: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.BooleanList, None, False, False, 10), ArgSingle('number_rb', number_rb, DataType.IntegerList, None, False, False, 10), ArgSingle('start_rb', start_rb, DataType.IntegerList, None, False, False, 10), ArgSingle('mcs', mcs, DataType.IntegerList, None, False, False, 10))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: List[bool]: No parameter help available
			- Number_Rb: List[int]: No parameter help available
			- Start_Rb: List[int]: No parameter help available
			- Mcs: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, False, 10),
			ArgStruct('Number_Rb', DataType.IntegerList, None, False, False, 10),
			ArgStruct('Start_Rb', DataType.IntegerList, None, False, False, 10),
			ArgStruct('Mcs', DataType.IntegerList, None, False, False, 10)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Number_Rb: List[int] = None
			self.Start_Rb: List[int] = None
			self.Mcs: List[int] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.all.get(cell_name = 'abc') \n
		Defines the scheduled RB allocation and the MCS index for all DL subframes. The parameters are entered 10 times, so that
		all subframes are configured by a single command (index = subframe number 0 to 9) : <CellName>, <Enable>0, ..., <Enable>9,
		<NumberRB>0, ..., <NumberRB>9, <StartRB>0, ..., <StartRB>9, <MCS>0, ..., <MCS>9 \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:ALL? {param}', self.__class__.GetStruct())
