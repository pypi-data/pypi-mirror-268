from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Enable: bool: Enables or disables scheduling for all UL slots.
			- Modulation: enums.ModulationB: Optional setting parameter. π/2-BPSK, QPSK, 16QAM, 64QAM, 256QAM
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Tp_Recoding: enums.Waveform: Optional setting parameter. OFDM type CP-OFDM or DFT-s-OFDM"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum_optional('Modulation', enums.ModulationB),
			ArgStruct.scalar_int_optional('Number_Rb'),
			ArgStruct.scalar_int_optional('Start_Rb'),
			ArgStruct.scalar_enum_optional('Tp_Recoding', enums.Waveform)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Enable: bool = None
			self.Modulation: enums.ModulationB = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Tp_Recoding: enums.Waveform = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:RMC:UL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.ueScheduling.rmc.uplink.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Enable: bool = False \n
		structure.Modulation: enums.ModulationB = enums.ModulationB.BPSK \n
		structure.Number_Rb: int = 1 \n
		structure.Start_Rb: int = 1 \n
		structure.Tp_Recoding: enums.Waveform = enums.Waveform.CP \n
		driver.configure.signaling.nradio.cell.ueScheduling.rmc.uplink.set(structure) \n
		Configures NR cell settings to values compliant with a UL RMC definition. A setting command accepts only certain value
		combinations. Use the RMC wizard in the GUI to get allowed value combinations. A query returns the set of values that is
		presented by the RMC wizard. These values can differ from currently applied values. Omit optional parameters only if you
		do not care which value you get (just any RMC-compliant value) . \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:RMC:UL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables or disables scheduling for all UL slots.
			- Modulation: enums.ModulationB: π/2-BPSK, QPSK, 16QAM, 64QAM, 256QAM
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Tp_Recoding: enums.Waveform: OFDM type CP-OFDM or DFT-s-OFDM"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Modulation', enums.ModulationB),
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Tp_Recoding', enums.Waveform)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Modulation: enums.ModulationB = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Tp_Recoding: enums.Waveform = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:RMC:UL \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ueScheduling.rmc.uplink.get(cell_name = 'abc') \n
		Configures NR cell settings to values compliant with a UL RMC definition. A setting command accepts only certain value
		combinations. Use the RMC wizard in the GUI to get allowed value combinations. A query returns the set of values that is
		presented by the RMC wizard. These values can differ from currently applied values. Omit optional parameters only if you
		do not care which value you get (just any RMC-compliant value) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:RMC:UL? {param}', self.__class__.GetStruct())
