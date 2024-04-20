from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Duplex_Mode: enums.DuplexModeB: No parameter help available
			- Fbi: int: Optional setting parameter. Frequency band indicator
			- Dl_Bw: enums.DlUlBandwidth: Optional setting parameter. DL carrier bandwidth in MHz
			- Dl_Frequency: float: Optional setting parameter. DL carrier center frequency
			- Ul_Bw: enums.DlUlBandwidth: Optional setting parameter. UL carrier bandwidth in MHz (ignored for TDD/SDL)
			- Ul_Frequency: float: Optional setting parameter. UL carrier center frequency (ignored for TDD/SDL)
			- Scs: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_int_optional('Fbi'),
			ArgStruct.scalar_enum_optional('Dl_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_float_optional('Dl_Frequency'),
			ArgStruct.scalar_enum_optional('Ul_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_float_optional('Ul_Frequency'),
			ArgStruct.scalar_int_optional('Scs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Fbi: int = None
			self.Dl_Bw: enums.DlUlBandwidth = None
			self.Dl_Frequency: float = None
			self.Ul_Bw: enums.DlUlBandwidth = None
			self.Ul_Frequency: float = None
			self.Scs: int = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:COMBined:CFRequency:FREQuency \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.rfSettings.combined.cfrequency.frequency.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Duplex_Mode: enums.DuplexModeB = enums.DuplexModeB.FDD \n
		structure.Fbi: int = 1 \n
		structure.Dl_Bw: enums.DlUlBandwidth = enums.DlUlBandwidth.B005 \n
		structure.Dl_Frequency: float = 1.0 \n
		structure.Ul_Bw: enums.DlUlBandwidth = enums.DlUlBandwidth.B005 \n
		structure.Ul_Frequency: float = 1.0 \n
		structure.Scs: int = 1 \n
		driver.configure.signaling.nradio.cell.rfSettings.combined.cfrequency.frequency.set(structure) \n
		Modifies several frequency settings simultaneously, for example, to change the frequency for an established connection,
		without losing the connection. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:COMBined:CFRequency:FREQuency', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Duplex_Mode: enums.DuplexModeB: No parameter help available
			- Fbi: int: Frequency band indicator
			- Dl_Bw: enums.DlUlBandwidth: DL carrier bandwidth in MHz
			- Dl_Frequency: float: DL carrier center frequency
			- Ul_Bw: enums.DlUlBandwidth: UL carrier bandwidth in MHz (ignored for TDD/SDL)
			- Ul_Frequency: float: UL carrier center frequency (ignored for TDD/SDL)
			- Scs: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_int('Fbi'),
			ArgStruct.scalar_enum('Dl_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_float('Dl_Frequency'),
			ArgStruct.scalar_enum('Ul_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_float('Ul_Frequency'),
			ArgStruct.scalar_int('Scs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Fbi: int = None
			self.Dl_Bw: enums.DlUlBandwidth = None
			self.Dl_Frequency: float = None
			self.Ul_Bw: enums.DlUlBandwidth = None
			self.Ul_Frequency: float = None
			self.Scs: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:COMBined:CFRequency:FREQuency \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.rfSettings.combined.cfrequency.frequency.get(cell_name = 'abc') \n
		Modifies several frequency settings simultaneously, for example, to change the frequency for an established connection,
		without losing the connection. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:COMBined:CFRequency:FREQuency? {param}', self.__class__.GetStruct())
