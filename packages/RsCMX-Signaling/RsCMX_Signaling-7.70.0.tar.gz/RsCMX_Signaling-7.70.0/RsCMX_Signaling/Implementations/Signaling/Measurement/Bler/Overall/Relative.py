from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


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
			- Ack: float: Number of received acknowledgments as percentage
			- Nack: float: Number of received negative acknowledgments as percentage
			- Dtx: float: Number of missing answers (no ACK, no NACK) as percentage
			- Bler: float: Block error ratio as percentage
			- Throughput_Avg: float: Average throughput as percentage of scheduled throughput"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ack'),
			ArgStruct.scalar_float('Nack'),
			ArgStruct.scalar_float('Dtx'),
			ArgStruct.scalar_float('Bler'),
			ArgStruct.scalar_float('Throughput_Avg')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ack: float = None
			self.Nack: float = None
			self.Dtx: float = None
			self.Bler: float = None
			self.Throughput_Avg: float = None

	def fetch(self, algorithm: enums.Algorithm = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:OVERall:RELative \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.overall.relative.fetch(algorithm = enums.Algorithm.ERC1) \n
		Returns the overall relative DL results of the BLER measurement. \n
			:param algorithm: Selects the formula for calculation of the BLER from the number of ACK, NACK and DTX. ERC1 (Default) : BLER = (NACK + DTX) / (ACK + NACK + DTX) ERC2: BLER = DTX / (ACK + NACK + DTX) ERC3: BLER = NACK / (ACK + NACK + DTX) ERC4: BLER = NACK / (ACK + NACK)
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('algorithm', algorithm, DataType.Enum, enums.Algorithm, is_optional=True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:OVERall:RELative? {param}'.rstrip(), self.__class__.FetchStruct())
