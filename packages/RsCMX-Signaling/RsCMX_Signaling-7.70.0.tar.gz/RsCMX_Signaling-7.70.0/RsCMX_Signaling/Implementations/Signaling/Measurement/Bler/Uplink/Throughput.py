from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThroughputCls:
	"""Throughput commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("throughput", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Cell_Name: List[str]: Name of the cell providing the measured connection
			- Rel_Crc_Passed: List[float]: Throughput as percentage of scheduled throughput
			- Abs_Crc_Passed: List[int]: Throughput in bit/s
			- Abs_Scheduled: List[int]: Scheduled throughput in bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Rel_Crc_Passed', DataType.FloatList, None, False, True, 1),
			ArgStruct('Abs_Crc_Passed', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Abs_Scheduled', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.Rel_Crc_Passed: List[float] = None
			self.Abs_Crc_Passed: List[int] = None
			self.Abs_Scheduled: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:UL:THRoughput \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.uplink.throughput.fetch() \n
		Returns the UL throughput results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <RelCRCPassed>, <AbsCRCPassed>, <AbsScheduled>}, {...}, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:UL:THRoughput?', self.__class__.FetchStruct())
