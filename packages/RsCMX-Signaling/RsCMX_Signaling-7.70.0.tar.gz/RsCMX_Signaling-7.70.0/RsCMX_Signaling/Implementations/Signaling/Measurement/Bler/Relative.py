from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelativeCls:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Cell_Name: List[str]: Name of the cell providing the measured connection
			- Ack: List[float]: Number of received acknowledgments as percentage
			- Nack: List[float]: Number of received negative acknowledgments as percentage
			- Dtx: List[float]: Number of missing answers (no ACK, no NACK) as percentage
			- Bler: List[float]: Block error ratio as percentage
			- Throughput_Avg: List[float]: Average throughput as percentage of scheduled throughput"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Ack', DataType.FloatList, None, False, True, 1),
			ArgStruct('Nack', DataType.FloatList, None, False, True, 1),
			ArgStruct('Dtx', DataType.FloatList, None, False, True, 1),
			ArgStruct('Bler', DataType.FloatList, None, False, True, 1),
			ArgStruct('Throughput_Avg', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.Ack: List[float] = None
			self.Nack: List[float] = None
			self.Dtx: List[float] = None
			self.Bler: List[float] = None
			self.Throughput_Avg: List[float] = None

	def fetch(self, algorithm: enums.Algorithm = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:RELative \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.relative.fetch(algorithm = enums.Algorithm.ERC1) \n
		Returns the relative DL results of the BLER measurement. There is one set of results {...} per cell: <Reliability>,
		{<CellName>, <ACK>, <NACK>, <DTX>, <BLER>, <ThroughputAvg>}, {...}, ... \n
			:param algorithm: Selects the formula for calculation of the BLER from the number of ACK, NACK and DTX. ERC1 (Default) : BLER = (NACK + DTX) / (ACK + NACK + DTX) ERC2: BLER = DTX / (ACK + NACK + DTX) ERC3: BLER = NACK / (ACK + NACK + DTX) ERC4: BLER = NACK / (ACK + NACK)
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('algorithm', algorithm, DataType.Enum, enums.Algorithm, is_optional=True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:RELative? {param}'.rstrip(), self.__class__.FetchStruct())
