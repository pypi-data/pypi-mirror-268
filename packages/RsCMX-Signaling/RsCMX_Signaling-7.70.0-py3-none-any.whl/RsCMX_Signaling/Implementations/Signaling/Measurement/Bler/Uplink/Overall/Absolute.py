from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


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
			- Crc_Passed: int: Number of passed CRC
			- Crc_Failed: int: Number of failed CRC
			- Dtx: int: Discontinuous transmissions"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Crc_Passed'),
			ArgStruct.scalar_int('Crc_Failed'),
			ArgStruct.scalar_int('Dtx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Crc_Passed: int = None
			self.Crc_Failed: int = None
			self.Dtx: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:UL:OVERall:ABSolute \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.uplink.overall.absolute.fetch() \n
		Returns the overall absolute UL results of the BLER measurement. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:UL:OVERall:ABSolute?', self.__class__.FetchStruct())
