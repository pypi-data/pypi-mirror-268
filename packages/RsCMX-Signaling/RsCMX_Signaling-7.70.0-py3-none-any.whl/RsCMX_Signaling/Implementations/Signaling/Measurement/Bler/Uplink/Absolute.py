from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


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
			- Crc_Failed: List[int]: Number of failed CRC
			- Crc_Passed: List[int]: Number of passed CRC
			- Dtx: List[int]: Discontinuous transmissions"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Crc_Failed', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Crc_Passed', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dtx', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.Crc_Failed: List[int] = None
			self.Crc_Passed: List[int] = None
			self.Dtx: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:UL:ABSolute \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.uplink.absolute.fetch() \n
		Returns the absolute UL results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <CRCFailed>, <CRCPassed>, <DTX>}, {...}, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:UL:ABSolute?', self.__class__.FetchStruct())
