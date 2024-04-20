from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CombinedCls:
	"""Combined commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("combined", core, parent)

	@property
	def location(self):
		"""location commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_location'):
			from .Location import LocationCls
			self._location = LocationCls(self._core, self._cmd_group)
		return self._location

	@property
	def cfrequency(self):
		"""cfrequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfrequency'):
			from .Cfrequency import CfrequencyCls
			self._cfrequency = CfrequencyCls(self._core, self._cmd_group)
		return self._cfrequency

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Duplex_Mode: enums.DuplexModeB: No parameter help available
			- Fbi: int: Optional setting parameter. Frequency band indicator
			- Dl_Bw: enums.DlUlBandwidth: Optional setting parameter. DL carrier bandwidth in MHz
			- Dl_Off_To_Carrier: int: Optional setting parameter. DL offset to carrier
			- Dl_Point_Aarfcn: int: Optional setting parameter. DL channel number (ARFCN) of point A
			- Ul_Bw: enums.DlUlBandwidth: Optional setting parameter. UL carrier bandwidth in MHz (ignored for TDD/SDL)
			- Ul_Off_To_Carrier: int: Optional setting parameter. UL offset to carrier (ignored for TDD/SDL)
			- Ul_Point_Aarfcn: int: Optional setting parameter. UL channel number (ARFCN) of point A (ignored for TDD/SDL)
			- Control_Zero: int: Optional setting parameter. Common control resource set (CORESET) number 0
			- Kssb: int: Optional setting parameter. Number of SC between the SSB and the overall RB grid (kSSB) .
			- Offset_Point_A: int: Optional setting parameter. Parameter 'offsetToPointA' of the SIB (number of RB)
			- Scs: int: Optional setting parameter. Subcarrier spacing"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_int_optional('Fbi'),
			ArgStruct.scalar_enum_optional('Dl_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_int_optional('Dl_Off_To_Carrier'),
			ArgStruct.scalar_int_optional('Dl_Point_Aarfcn'),
			ArgStruct.scalar_enum_optional('Ul_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_int_optional('Ul_Off_To_Carrier'),
			ArgStruct.scalar_int_optional('Ul_Point_Aarfcn'),
			ArgStruct.scalar_int_optional('Control_Zero'),
			ArgStruct.scalar_int_optional('Kssb'),
			ArgStruct.scalar_int_optional('Offset_Point_A'),
			ArgStruct.scalar_int_optional('Scs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Fbi: int = None
			self.Dl_Bw: enums.DlUlBandwidth = None
			self.Dl_Off_To_Carrier: int = None
			self.Dl_Point_Aarfcn: int = None
			self.Ul_Bw: enums.DlUlBandwidth = None
			self.Ul_Off_To_Carrier: int = None
			self.Ul_Point_Aarfcn: int = None
			self.Control_Zero: int = None
			self.Kssb: int = None
			self.Offset_Point_A: int = None
			self.Scs: int = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:COMBined \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.rfSettings.combined.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Duplex_Mode: enums.DuplexModeB = enums.DuplexModeB.FDD \n
		structure.Fbi: int = 1 \n
		structure.Dl_Bw: enums.DlUlBandwidth = enums.DlUlBandwidth.B005 \n
		structure.Dl_Off_To_Carrier: int = 1 \n
		structure.Dl_Point_Aarfcn: int = 1 \n
		structure.Ul_Bw: enums.DlUlBandwidth = enums.DlUlBandwidth.B005 \n
		structure.Ul_Off_To_Carrier: int = 1 \n
		structure.Ul_Point_Aarfcn: int = 1 \n
		structure.Control_Zero: int = 1 \n
		structure.Kssb: int = 1 \n
		structure.Offset_Point_A: int = 1 \n
		structure.Scs: int = 1 \n
		driver.configure.signaling.nradio.cell.rfSettings.combined.set(structure) \n
		Modifies several frequency settings simultaneously, for example, to change the frequency for an established connection,
		without losing the connection. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:COMBined', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Duplex_Mode: enums.DuplexModeB: No parameter help available
			- Fbi: int: Frequency band indicator
			- Dl_Bw: enums.DlUlBandwidth: DL carrier bandwidth in MHz
			- Dl_Off_To_Carrier: int: DL offset to carrier
			- Dl_Point_Aarfcn: int: DL channel number (ARFCN) of point A
			- Ul_Bw: enums.DlUlBandwidth: UL carrier bandwidth in MHz (ignored for TDD/SDL)
			- Ul_Off_To_Carrier: int: UL offset to carrier (ignored for TDD/SDL)
			- Ul_Point_Aarfcn: int: UL channel number (ARFCN) of point A (ignored for TDD/SDL)
			- Control_Zero: int: Common control resource set (CORESET) number 0
			- Kssb: int: Number of SC between the SSB and the overall RB grid (kSSB) .
			- Offset_Point_A: int: Parameter 'offsetToPointA' of the SIB (number of RB)
			- Scs: int: Subcarrier spacing"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_int('Fbi'),
			ArgStruct.scalar_enum('Dl_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_int('Dl_Off_To_Carrier'),
			ArgStruct.scalar_int('Dl_Point_Aarfcn'),
			ArgStruct.scalar_enum('Ul_Bw', enums.DlUlBandwidth),
			ArgStruct.scalar_int('Ul_Off_To_Carrier'),
			ArgStruct.scalar_int('Ul_Point_Aarfcn'),
			ArgStruct.scalar_int('Control_Zero'),
			ArgStruct.scalar_int('Kssb'),
			ArgStruct.scalar_int('Offset_Point_A'),
			ArgStruct.scalar_int('Scs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Fbi: int = None
			self.Dl_Bw: enums.DlUlBandwidth = None
			self.Dl_Off_To_Carrier: int = None
			self.Dl_Point_Aarfcn: int = None
			self.Ul_Bw: enums.DlUlBandwidth = None
			self.Ul_Off_To_Carrier: int = None
			self.Ul_Point_Aarfcn: int = None
			self.Control_Zero: int = None
			self.Kssb: int = None
			self.Offset_Point_A: int = None
			self.Scs: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:COMBined \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.rfSettings.combined.get(cell_name = 'abc') \n
		Modifies several frequency settings simultaneously, for example, to change the frequency for an established connection,
		without losing the connection. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:COMBined? {param}', self.__class__.GetStruct())

	def clone(self) -> 'CombinedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CombinedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
