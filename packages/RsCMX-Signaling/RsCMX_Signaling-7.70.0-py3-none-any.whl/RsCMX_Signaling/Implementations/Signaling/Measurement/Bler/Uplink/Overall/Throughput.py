from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


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
			- Rel_Avg: float: Throughput as percentage of scheduled throughput
			- Abs_Crc_Passed: int: Throughput in bit/s
			- Abs_Scheduled: int: Scheduled throughput in bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Rel_Avg'),
			ArgStruct.scalar_int('Abs_Crc_Passed'),
			ArgStruct.scalar_int('Abs_Scheduled')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rel_Avg: float = None
			self.Abs_Crc_Passed: int = None
			self.Abs_Scheduled: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:UL:OVERall:THRoughput \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.uplink.overall.throughput.fetch() \n
		Returns the overall UL throughput results of the BLER measurement. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:UL:OVERall:THRoughput?', self.__class__.FetchStruct())
