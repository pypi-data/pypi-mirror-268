from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LocationCls:
	"""Location commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("location", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Duplex_Mode: enums.DuplexModeB: No parameter help available
			- Fbi: int: Optional setting parameter. Frequency band indicator
			- Dl_Bw: enums.DlUlBandwidth: Optional setting parameter. DL carrier bandwidth in MHz
			- Dl_Location: enums.DlUlLocation: Optional setting parameter. DL frequency
				- MID, LOW, HIGH: Automatic selection of mid, low or high position in the frequency band.
				- USER: User-defined frequency, specified via a separate command.
			- Ul_Bw: enums.DlUlBandwidth: Optional setting parameter. UL carrier bandwidth in MHz (ignored for TDD/SDL)
			- Ul_Location: enums.DlUlLocation: Optional setting parameter. UL frequency (ignored for TDD/SDL)
				- MID, LOW, HIGH: Automatic selection of mid, low or high position in the frequency band.
				- USER: User-defined frequency, specified via a separate command.
			- Scs: int: Optional setting parameter. Subcarrier spacing"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_int_optional('Fbi'),
			ArgStruct.scalar_enum_optional('Dl_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_enum_optional('Dl_Location', enums.DlUlLocation),
			ArgStruct.scalar_enum_optional('Ul_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_enum_optional('Ul_Location', enums.DlUlLocation),
			ArgStruct.scalar_int_optional('Scs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Fbi: int = None
			self.Dl_Bw: enums.DlUlBandwidth = None
			self.Dl_Location: enums.DlUlLocation = None
			self.Ul_Bw: enums.DlUlBandwidth = None
			self.Ul_Location: enums.DlUlLocation = None
			self.Scs: int = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:COMBined:LOCation \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.rfSettings.combined.location.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Duplex_Mode: enums.DuplexModeB = enums.DuplexModeB.FDD \n
		structure.Fbi: int = 1 \n
		structure.Dl_Bw: enums.DlUlBandwidth = enums.DlUlBandwidth.B005 \n
		structure.Dl_Location: enums.DlUlLocation = enums.DlUlLocation.HIGH \n
		structure.Ul_Bw: enums.DlUlBandwidth = enums.DlUlBandwidth.B005 \n
		structure.Ul_Location: enums.DlUlLocation = enums.DlUlLocation.HIGH \n
		structure.Scs: int = 1 \n
		driver.configure.signaling.nradio.cell.rfSettings.combined.location.set(structure) \n
		Modifies several frequency settings simultaneously, for example, to change the frequency for an established connection,
		without losing the connection. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:COMBined:LOCation', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Duplex_Mode: enums.DuplexModeB: No parameter help available
			- Fbi: int: Frequency band indicator
			- Dl_Bw: enums.DlUlBandwidth: DL carrier bandwidth in MHz
			- Dl_Location: enums.DlUlLocation: DL frequency
				- MID, LOW, HIGH: Automatic selection of mid, low or high position in the frequency band.
				- USER: User-defined frequency, specified via a separate command.
			- Ul_Bw: enums.DlUlBandwidth: UL carrier bandwidth in MHz (ignored for TDD/SDL)
			- Ul_Location: enums.DlUlLocation: UL frequency (ignored for TDD/SDL)
				- MID, LOW, HIGH: Automatic selection of mid, low or high position in the frequency band.
				- USER: User-defined frequency, specified via a separate command.
			- Scs: int: Subcarrier spacing"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_int('Fbi'),
			ArgStruct.scalar_enum('Dl_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_enum('Dl_Location', enums.DlUlLocation),
			ArgStruct.scalar_enum('Ul_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_enum('Ul_Location', enums.DlUlLocation),
			ArgStruct.scalar_int('Scs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Fbi: int = None
			self.Dl_Bw: enums.DlUlBandwidth = None
			self.Dl_Location: enums.DlUlLocation = None
			self.Ul_Bw: enums.DlUlBandwidth = None
			self.Ul_Location: enums.DlUlLocation = None
			self.Scs: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:COMBined:LOCation \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.rfSettings.combined.location.get(cell_name = 'abc') \n
		Modifies several frequency settings simultaneously, for example, to change the frequency for an established connection,
		without losing the connection. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:COMBined:LOCation? {param}', self.__class__.GetStruct())
