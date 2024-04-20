from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpEnableCls:
	"""TpEnable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpEnable", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Sample_Dens_Nrb_0: int: Signaled 'sampleDensity', NRB0.
			- Sample_Dens_Nrb_1: int: Signaled 'sampleDensity', NRB1.
			- Sample_Dens_Nrb_2: int: Signaled 'sampleDensity', NRB2.
			- Sample_Dens_Nrb_3: int: Signaled 'sampleDensity', NRB3.
			- Sample_Dens_Nrb_4: int: Signaled 'sampleDensity', NRB4.
			- Tp_Time_Dens: enums.TpTimeDens: Signaled 'timeDensityTransformPrecoding'."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_0'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_1'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_2'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_3'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_4'),
			ArgStruct.scalar_enum('Tp_Time_Dens', enums.TpTimeDens)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Sample_Dens_Nrb_0: int = None
			self.Sample_Dens_Nrb_1: int = None
			self.Sample_Dens_Nrb_2: int = None
			self.Sample_Dens_Nrb_3: int = None
			self.Sample_Dens_Nrb_4: int = None
			self.Tp_Time_Dens: enums.TpTimeDens = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPENable \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.dmrs.uplink.ptrs.tpEnable.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Sample_Dens_Nrb_0: int = 1 \n
		structure.Sample_Dens_Nrb_1: int = 1 \n
		structure.Sample_Dens_Nrb_2: int = 1 \n
		structure.Sample_Dens_Nrb_3: int = 1 \n
		structure.Sample_Dens_Nrb_4: int = 1 \n
		structure.Tp_Time_Dens: enums.TpTimeDens = enums.TpTimeDens.D2 \n
		driver.configure.signaling.nradio.cell.dmrs.uplink.ptrs.tpEnable.set(structure) \n
		Defines the IE 'PTRS-UplinkConfig' for signals with transform precoding, initial BWP. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPENable', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sample_Dens_Nrb_0: int: Signaled 'sampleDensity', NRB0.
			- Sample_Dens_Nrb_1: int: Signaled 'sampleDensity', NRB1.
			- Sample_Dens_Nrb_2: int: Signaled 'sampleDensity', NRB2.
			- Sample_Dens_Nrb_3: int: Signaled 'sampleDensity', NRB3.
			- Sample_Dens_Nrb_4: int: Signaled 'sampleDensity', NRB4.
			- Tp_Time_Dens: enums.TpTimeDens: Signaled 'timeDensityTransformPrecoding'."""
		__meta_args_list = [
			ArgStruct.scalar_int('Sample_Dens_Nrb_0'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_1'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_2'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_3'),
			ArgStruct.scalar_int('Sample_Dens_Nrb_4'),
			ArgStruct.scalar_enum('Tp_Time_Dens', enums.TpTimeDens)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sample_Dens_Nrb_0: int = None
			self.Sample_Dens_Nrb_1: int = None
			self.Sample_Dens_Nrb_2: int = None
			self.Sample_Dens_Nrb_3: int = None
			self.Sample_Dens_Nrb_4: int = None
			self.Tp_Time_Dens: enums.TpTimeDens = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPENable \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.dmrs.uplink.ptrs.tpEnable.get(cell_name = 'abc') \n
		Defines the IE 'PTRS-UplinkConfig' for signals with transform precoding, initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:PTRS:TPENable? {param}', self.__class__.GetStruct())
