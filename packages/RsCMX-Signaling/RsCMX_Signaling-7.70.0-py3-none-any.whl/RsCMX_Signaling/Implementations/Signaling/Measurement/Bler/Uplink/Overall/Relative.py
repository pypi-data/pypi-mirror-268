from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


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
			- Crc_Passed: float: Number of passed CRC as a percentage
			- Crc_Failed: float: Number of failed CRC as a percentage
			- Dtx: float: Discontinuous transmissions as a percentage
			- Bler: float: Block error ratio as a percentage"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Crc_Passed'),
			ArgStruct.scalar_float('Crc_Failed'),
			ArgStruct.scalar_float('Dtx'),
			ArgStruct.scalar_float('Bler')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Crc_Passed: float = None
			self.Crc_Failed: float = None
			self.Dtx: float = None
			self.Bler: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:UL:OVERall:RELative \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.uplink.overall.relative.fetch() \n
		Returns the overall relative UL results of the BLER measurement. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:UL:OVERall:RELative?', self.__class__.FetchStruct())
