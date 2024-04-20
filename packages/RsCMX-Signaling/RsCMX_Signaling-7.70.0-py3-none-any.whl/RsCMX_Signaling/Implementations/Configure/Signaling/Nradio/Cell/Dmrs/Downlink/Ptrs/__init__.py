from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtrsCls:
	"""Ptrs commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptrs", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

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
			- Epre_Ratio: enums.EpreRatio: Signaled 'epre-Ratio', PTRS relative to PDSCH.
			- Resource_Offset: enums.ResourceOffset: Signaled 'resourceElementOffset'."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Time_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Time_Dens_Mcs_1'),
			ArgStruct.scalar_int('Time_Dens_Mcs_2'),
			ArgStruct.scalar_int('Time_Dens_Mcs_3'),
			ArgStruct.scalar_enum('Freq_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Freq_Dens_Nrb_0'),
			ArgStruct.scalar_int('Freq_Dens_Nrb_1'),
			ArgStruct.scalar_enum('Epre_Ratio', enums.EpreRatio),
			ArgStruct.scalar_enum('Resource_Offset', enums.ResourceOffset)]

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
			self.Epre_Ratio: enums.EpreRatio = None
			self.Resource_Offset: enums.ResourceOffset = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:DL:PTRS \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.dmrs.downlink.ptrs.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Time_Dens_Pres: enums.DensityPreset = enums.DensityPreset.NPResent \n
		structure.Time_Dens_Mcs_1: int = 1 \n
		structure.Time_Dens_Mcs_2: int = 1 \n
		structure.Time_Dens_Mcs_3: int = 1 \n
		structure.Freq_Dens_Pres: enums.DensityPreset = enums.DensityPreset.NPResent \n
		structure.Freq_Dens_Nrb_0: int = 1 \n
		structure.Freq_Dens_Nrb_1: int = 1 \n
		structure.Epre_Ratio: enums.EpreRatio = enums.EpreRatio.R0 \n
		structure.Resource_Offset: enums.ResourceOffset = enums.ResourceOffset.NPResent \n
		driver.configure.signaling.nradio.cell.dmrs.downlink.ptrs.set(structure) \n
		Defines the IE 'PTRS-DownlinkConfig' for initial BWP. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:DL:PTRS', structure)

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
			- Epre_Ratio: enums.EpreRatio: Signaled 'epre-Ratio', PTRS relative to PDSCH.
			- Resource_Offset: enums.ResourceOffset: Signaled 'resourceElementOffset'."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Time_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Time_Dens_Mcs_1'),
			ArgStruct.scalar_int('Time_Dens_Mcs_2'),
			ArgStruct.scalar_int('Time_Dens_Mcs_3'),
			ArgStruct.scalar_enum('Freq_Dens_Pres', enums.DensityPreset),
			ArgStruct.scalar_int('Freq_Dens_Nrb_0'),
			ArgStruct.scalar_int('Freq_Dens_Nrb_1'),
			ArgStruct.scalar_enum('Epre_Ratio', enums.EpreRatio),
			ArgStruct.scalar_enum('Resource_Offset', enums.ResourceOffset)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Time_Dens_Pres: enums.DensityPreset = None
			self.Time_Dens_Mcs_1: int = None
			self.Time_Dens_Mcs_2: int = None
			self.Time_Dens_Mcs_3: int = None
			self.Freq_Dens_Pres: enums.DensityPreset = None
			self.Freq_Dens_Nrb_0: int = None
			self.Freq_Dens_Nrb_1: int = None
			self.Epre_Ratio: enums.EpreRatio = None
			self.Resource_Offset: enums.ResourceOffset = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:DL:PTRS \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.dmrs.downlink.ptrs.get(cell_name = 'abc') \n
		Defines the IE 'PTRS-DownlinkConfig' for initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:DL:PTRS? {param}', self.__class__.GetStruct())

	def clone(self) -> 'PtrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PtrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
