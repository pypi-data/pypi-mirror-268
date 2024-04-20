from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpDisableCls:
	"""TpDisable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpDisable", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Time_Dens_Pres: enums.DensityPreset: Presence of the 'timeDensity' (field signaled or not) .
			- Time_Dens_Mcs_1: int: Signaled 'timeDensity', ptrs-MCS1.
			- Time_Dens_Mcs_2: int: Signaled 'timeDensity', ptrs-MCS2.
			- Time_Dens_Mcs_3: int: Signaled 'timeDensity', ptrs-MCS3.
			- Freq_Dens_Pres: enums.DensityPreset: Presence of the 'frequencyDensity' (field signaled or not) .
			- Freq_Dens_Nrb_0: int: Signaled 'frequencyDensity', NRB0.
			- Freq_Dens_Nrb_1: int: Signaled 'frequencyDensity', NRB1.
			- Max_Ports: enums.MaxPorts: Signaled 'maxNrofPorts'.
			- Resource_Offset: enums.ResourceOffset: Signaled 'resourceElementOffset'.
			- Power: enums.PtrsPower: Signaled 'ptrs-Power'."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Time_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Time_Dens_Mcs_1'),
			ArgStruct.scalar_int('Time_Dens_Mcs_2'),
			ArgStruct.scalar_int('Time_Dens_Mcs_3'),
			ArgStruct.scalar_enum('Freq_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Freq_Dens_Nrb_0'),
			ArgStruct.scalar_int('Freq_Dens_Nrb_1'),
			ArgStruct.scalar_enum('Max_Ports', enums.MaxPorts),
			ArgStruct.scalar_enum('Resource_Offset', enums.ResourceOffset),
			ArgStruct.scalar_enum('Power', enums.PtrsPower)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Time_Dens_Pres: enums.DensityPreset = None
			self.Time_Dens_Mcs_1: int = None
			self.Time_Dens_Mcs_2: int = None
			self.Time_Dens_Mcs_3: int = None
			self.Freq_Dens_Pres: enums.DensityPreset = None
			self.Freq_Dens_Nrb_0: int = None
			self.Freq_Dens_Nrb_1: int = None
			self.Max_Ports: enums.MaxPorts = None
			self.Resource_Offset: enums.ResourceOffset = None
			self.Power: enums.PtrsPower = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPDisable \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.dmrs.uplink.ptrs.tpDisable.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Time_Dens_Pres: enums.DensityPreset = enums.DensityPreset.NPResent \n
		structure.Time_Dens_Mcs_1: int = 1 \n
		structure.Time_Dens_Mcs_2: int = 1 \n
		structure.Time_Dens_Mcs_3: int = 1 \n
		structure.Freq_Dens_Pres: enums.DensityPreset = enums.DensityPreset.NPResent \n
		structure.Freq_Dens_Nrb_0: int = 1 \n
		structure.Freq_Dens_Nrb_1: int = 1 \n
		structure.Max_Ports: enums.MaxPorts = enums.MaxPorts.N1 \n
		structure.Resource_Offset: enums.ResourceOffset = enums.ResourceOffset.NPResent \n
		structure.Power: enums.PtrsPower = enums.PtrsPower.P00 \n
		driver.configure.signaling.nradio.cell.dmrs.uplink.ptrs.tpDisable.set(structure) \n
		Defines the IE 'PTRS-UplinkConfig' for signals without transform precoding, initial BWP. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPDisable', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Time_Dens_Pres: enums.DensityPreset: Presence of the 'timeDensity' (field signaled or not) .
			- Time_Dens_Mcs_1: int: Signaled 'timeDensity', ptrs-MCS1.
			- Time_Dens_Mcs_2: int: Signaled 'timeDensity', ptrs-MCS2.
			- Time_Dens_Mcs_3: int: Signaled 'timeDensity', ptrs-MCS3.
			- Freq_Dens_Pres: enums.DensityPreset: Presence of the 'frequencyDensity' (field signaled or not) .
			- Freq_Dens_Nrb_0: int: Signaled 'frequencyDensity', NRB0.
			- Freq_Dens_Nrb_1: int: Signaled 'frequencyDensity', NRB1.
			- Max_Ports: enums.MaxPorts: Signaled 'maxNrofPorts'.
			- Resource_Offset: enums.ResourceOffset: Signaled 'resourceElementOffset'.
			- Power: enums.PtrsPower: Signaled 'ptrs-Power'."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Time_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Time_Dens_Mcs_1'),
			ArgStruct.scalar_int('Time_Dens_Mcs_2'),
			ArgStruct.scalar_int('Time_Dens_Mcs_3'),
			ArgStruct.scalar_enum('Freq_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Freq_Dens_Nrb_0'),
			ArgStruct.scalar_int('Freq_Dens_Nrb_1'),
			ArgStruct.scalar_enum('Max_Ports', enums.MaxPorts),
			ArgStruct.scalar_enum('Resource_Offset', enums.ResourceOffset),
			ArgStruct.scalar_enum('Power', enums.PtrsPower)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Time_Dens_Pres: enums.DensityPreset = None
			self.Time_Dens_Mcs_1: int = None
			self.Time_Dens_Mcs_2: int = None
			self.Time_Dens_Mcs_3: int = None
			self.Freq_Dens_Pres: enums.DensityPreset = None
			self.Freq_Dens_Nrb_0: int = None
			self.Freq_Dens_Nrb_1: int = None
			self.Max_Ports: enums.MaxPorts = None
			self.Resource_Offset: enums.ResourceOffset = None
			self.Power: enums.PtrsPower = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPDisable \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.dmrs.uplink.ptrs.tpDisable.get(cell_name = 'abc') \n
		Defines the IE 'PTRS-UplinkConfig' for signals without transform precoding, initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPDisable? {param}', self.__class__.GetStruct())
