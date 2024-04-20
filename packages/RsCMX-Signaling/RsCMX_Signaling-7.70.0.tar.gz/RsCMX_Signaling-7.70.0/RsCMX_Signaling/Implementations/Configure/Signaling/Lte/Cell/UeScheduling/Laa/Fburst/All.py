from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
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
			- Burst_Length: int: No parameter help available
			- First_Subframe: int: No parameter help available
			- Initial_Sf_Alloc: enums.InitialSfAlloc: Optional setting parameter. Initial subframe with full allocation (S0) or second slot only (S7)
			- Ofdm_Symbols: enums.OfdmSymbols: Optional setting parameter. OFDM symbols in last subframe of burst
			- Ccrntis_End: enums.CcrntisEnd: Optional setting parameter. Send CC-RNTI: F2SF: final 2 SF LSF: last SF BLSF: before last SF SASF: skip all SF ASF: all SF
			- Pdcch_Format: enums.PdcchFormatB: Optional setting parameter. Number of CCE for PDCCH scrambled with CC-RNTI."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int_optional('Periodicity'),
			ArgStruct.scalar_int_optional('Burst_Length'),
			ArgStruct.scalar_int_optional('First_Subframe'),
			ArgStruct.scalar_enum_optional('Initial_Sf_Alloc', enums.InitialSfAlloc),
			ArgStruct.scalar_enum_optional('Ofdm_Symbols', enums.OfdmSymbols),
			ArgStruct.scalar_enum_optional('Ccrntis_End', enums.CcrntisEnd),
			ArgStruct.scalar_enum_optional('Pdcch_Format', enums.PdcchFormatB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Periodicity: int = None
			self.Burst_Length: int = None
			self.First_Subframe: int = None
			self.Initial_Sf_Alloc: enums.InitialSfAlloc = None
			self.Ofdm_Symbols: enums.OfdmSymbols = None
			self.Ccrntis_End: enums.CcrntisEnd = None
			self.Pdcch_Format: enums.PdcchFormatB = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Periodicity: int = 1 \n
		structure.Burst_Length: int = 1 \n
		structure.First_Subframe: int = 1 \n
		structure.Initial_Sf_Alloc: enums.InitialSfAlloc = enums.InitialSfAlloc.S0 \n
		structure.Ofdm_Symbols: enums.OfdmSymbols = enums.OfdmSymbols.ALL \n
		structure.Ccrntis_End: enums.CcrntisEnd = enums.CcrntisEnd.ASF \n
		structure.Pdcch_Format: enums.PdcchFormatB = enums.PdcchFormatB.N1 \n
		driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.all.set(structure) \n
		Configures fixed bursts (combination of the other ...:FBURst:... commands) . \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Periodicity: int: No parameter help available
			- Burst_Length: int: No parameter help available
			- First_Subframe: int: No parameter help available
			- Initial_Sf_Alloc: enums.InitialSfAlloc: Initial subframe with full allocation (S0) or second slot only (S7)
			- Ofdm_Symbols: enums.OfdmSymbols: OFDM symbols in last subframe of burst
			- Ccrntis_End: enums.CcrntisEnd: Send CC-RNTI: F2SF: final 2 SF LSF: last SF BLSF: before last SF SASF: skip all SF ASF: all SF
			- Pdcch_Format: enums.PdcchFormatB: Number of CCE for PDCCH scrambled with CC-RNTI."""
		__meta_args_list = [
			ArgStruct.scalar_int('Periodicity'),
			ArgStruct.scalar_int('Burst_Length'),
			ArgStruct.scalar_int('First_Subframe'),
			ArgStruct.scalar_enum('Initial_Sf_Alloc', enums.InitialSfAlloc),
			ArgStruct.scalar_enum('Ofdm_Symbols', enums.OfdmSymbols),
			ArgStruct.scalar_enum('Ccrntis_End', enums.CcrntisEnd),
			ArgStruct.scalar_enum('Pdcch_Format', enums.PdcchFormatB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Periodicity: int = None
			self.Burst_Length: int = None
			self.First_Subframe: int = None
			self.Initial_Sf_Alloc: enums.InitialSfAlloc = None
			self.Ofdm_Symbols: enums.OfdmSymbols = None
			self.Ccrntis_End: enums.CcrntisEnd = None
			self.Pdcch_Format: enums.PdcchFormatB = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.all.get(cell_name = 'abc') \n
		Configures fixed bursts (combination of the other ...:FBURst:... commands) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ALL? {param}', self.__class__.GetStruct())
