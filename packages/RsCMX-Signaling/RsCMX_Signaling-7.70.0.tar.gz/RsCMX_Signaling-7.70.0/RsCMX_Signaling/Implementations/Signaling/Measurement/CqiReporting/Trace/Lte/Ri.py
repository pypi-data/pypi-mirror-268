from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RiCls:
	"""Ri commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ri", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Cell_Name: List[str]: Name of the cell for which the values are reported.
			- Count: List[int]: Number of returned values.
			- Value: List[int]: Comma-separated list of Count values, indicating how often the RI values 1 to Count have been reported."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Count', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Value', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.Count: List[int] = None
			self.Value: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:CQIReporting:TRACe:LTE:RI \n
		Snippet: value: FetchStruct = driver.signaling.measurement.cqiReporting.trace.lte.ri.fetch() \n
		Returns the contents of the histogram of reported RI values. There is one set of results {...
		} per LTE cell: <Reliability>, {<CellName>, <Count>, <Value>RI 1, ..., <Value>RI <Count>}, {...}, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:CQIReporting:TRACe:LTE:RI?', self.__class__.FetchStruct())
