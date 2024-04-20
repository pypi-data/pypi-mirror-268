from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfidenceCls:
	"""Confidence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("confidence", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Cell_Name: List[str]: Name of the cell providing the measured connection
			- State: List[enums.BlerState]: PENDing: measurement still running, no verdict yet PASS, FAIL: verdict of the measurement"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('State', DataType.EnumList, enums.BlerState, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.State: List[enums.BlerState] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:CONFidence \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.confidence.fetch() \n
		Returns the results of a confidence BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <State>}, {...}, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:CONFidence?', self.__class__.FetchStruct())
