from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbsoluteCls:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Cell_Name: List[str]: Name of the cell providing the measured connection
			- Ack: List[int]: Number of received acknowledgments
			- Nack: List[int]: Number of received negative acknowledgments
			- Dtx: List[int]: Number of missing answers (no ACK, no NACK)
			- Throughput_Avg: List[int]: Average throughput in bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Ack', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Nack', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dtx', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Throughput_Avg', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.Ack: List[int] = None
			self.Nack: List[int] = None
			self.Dtx: List[int] = None
			self.Throughput_Avg: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:ABSolute \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.absolute.fetch() \n
		Returns the absolute DL results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <ACK>, <NACK>, <DTX>, <ThroughputAvg>}, {...}, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:ABSolute?', self.__class__.FetchStruct())
