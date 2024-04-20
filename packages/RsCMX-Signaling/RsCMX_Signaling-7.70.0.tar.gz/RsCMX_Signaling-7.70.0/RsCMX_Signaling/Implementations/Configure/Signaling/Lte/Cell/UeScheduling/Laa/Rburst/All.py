from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Periodicity: int: No parameter help available
			- Ccrntis_End: enums.CcrntisEnd: Optional setting parameter. Send CC-RNTI: F2SF: final 2 SF LSF: last SF BLSF: before last SF SASF: skip all SF ASF: all SF
			- Pdcch_Format: enums.PdcchFormatB: Optional setting parameter. Number of CCE for PDCCH scrambled with CC-RNTI.
			- Bl_Count: int: Optional setting parameter. Number of values for BurstLength
			- Scount: int: Optional setting parameter. Number of values for Symbols
			- Burst_Length: List[int]: Optional setting parameter. Comma-separated list of all allowed values for the number of subframes in a random burst
			- Symbols: List[int]: Optional setting parameter. Comma-separated list of all allowed values for the number of allocated OFDM symbols in the last subframe"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int_optional('Periodicity'),
			ArgStruct.scalar_enum_optional('Ccrntis_End', enums.CcrntisEnd),
			ArgStruct.scalar_enum_optional('Pdcch_Format', enums.PdcchFormatB),
			ArgStruct.scalar_int_optional('Bl_Count'),
			ArgStruct.scalar_int_optional('Scount'),
			ArgStruct('Burst_Length', DataType.IntegerList, None, True, True, 1),
			ArgStruct('Symbols', DataType.IntegerList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Periodicity: int = None
			self.Ccrntis_End: enums.CcrntisEnd = None
			self.Pdcch_Format: enums.PdcchFormatB = None
			self.Bl_Count: int = None
			self.Scount: int = None
			self.Burst_Length: List[int] = None
			self.Symbols: List[int] = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Periodicity: int = 1 \n
		structure.Ccrntis_End: enums.CcrntisEnd = enums.CcrntisEnd.ASF \n
		structure.Pdcch_Format: enums.PdcchFormatB = enums.PdcchFormatB.N1 \n
		structure.Bl_Count: int = 1 \n
		structure.Scount: int = 1 \n
		structure.Burst_Length: List[int] = [1, 2, 3] \n
		structure.Symbols: List[int] = [1, 2, 3] \n
		driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.all.set(structure) \n
		This command combines the other ...:RBURst:... commands to configure random bursts. A query returns: <Periodicity>,
		<BTRatio>, <IPSRatio>, <CCRNTISend>, <PDCCHFormat>, <BLCount>, <SCount>, <BurstLength>, <Symbols> \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Periodicity: int: No parameter help available
			- Bt_Ratio: float: Burst transmission probability
			- Ips_Ratio: float: Initial partial subframes probability
			- Ccrntis_End: enums.CcrntisEnd: Send CC-RNTI: F2SF: final 2 SF LSF: last SF BLSF: before last SF SASF: skip all SF ASF: all SF
			- Pdcch_Format: enums.PdcchFormatB: Number of CCE for PDCCH scrambled with CC-RNTI.
			- Bl_Count: int: Number of values for BurstLength
			- Scount: int: Number of values for Symbols
			- Burst_Length: List[int]: Comma-separated list of all allowed values for the number of subframes in a random burst
			- Symbols: List[int]: Comma-separated list of all allowed values for the number of allocated OFDM symbols in the last subframe"""
		__meta_args_list = [
			ArgStruct.scalar_int('Periodicity'),
			ArgStruct.scalar_float('Bt_Ratio'),
			ArgStruct.scalar_float('Ips_Ratio'),
			ArgStruct.scalar_enum('Ccrntis_End', enums.CcrntisEnd),
			ArgStruct.scalar_enum('Pdcch_Format', enums.PdcchFormatB),
			ArgStruct.scalar_int('Bl_Count'),
			ArgStruct.scalar_int('Scount'),
			ArgStruct('Burst_Length', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Symbols', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Periodicity: int = None
			self.Bt_Ratio: float = None
			self.Ips_Ratio: float = None
			self.Ccrntis_End: enums.CcrntisEnd = None
			self.Pdcch_Format: enums.PdcchFormatB = None
			self.Bl_Count: int = None
			self.Scount: int = None
			self.Burst_Length: List[int] = None
			self.Symbols: List[int] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.all.get(cell_name = 'abc') \n
		This command combines the other ...:RBURst:... commands to configure random bursts. A query returns: <Periodicity>,
		<BTRatio>, <IPSRatio>, <CCRNTISend>, <PDCCHFormat>, <BLCount>, <SCount>, <BurstLength>, <Symbols> \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:ALL? {param}', self.__class__.GetStruct())
