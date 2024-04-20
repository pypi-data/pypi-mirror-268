from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import enums


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
			- Slot: int: Optional setting parameter. Slot for sending the DCI that enables UL CG.
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Mcs: int: No parameter help available
			- Start_Symbol: int: No parameter help available
			- Number_Symbol: int: No parameter help available
			- Mapping: enums.Mapping: Optional setting parameter. Type of PUSCH mapping
			- Offset: int: Optional setting parameter. Slot offset k2 for the PUSCH"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int_optional('Slot'),
			ArgStruct.scalar_int_optional('Number_Rb'),
			ArgStruct.scalar_int_optional('Start_Rb'),
			ArgStruct.scalar_int_optional('Mcs'),
			ArgStruct.scalar_int_optional('Start_Symbol'),
			ArgStruct.scalar_int_optional('Number_Symbol'),
			ArgStruct.scalar_enum_optional('Mapping', enums.Mapping),
			ArgStruct.scalar_int_optional('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Slot: int = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Mcs: int = None
			self.Start_Symbol: int = None
			self.Number_Symbol: int = None
			self.Mapping: enums.Mapping = None
			self.Offset: int = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Slot: int = 1 \n
		structure.Number_Rb: int = 1 \n
		structure.Start_Rb: int = 1 \n
		structure.Mcs: int = 1 \n
		structure.Start_Symbol: int = 1 \n
		structure.Number_Symbol: int = 1 \n
		structure.Mapping: enums.Mapping = enums.Mapping.A \n
		structure.Offset: int = 1 \n
		driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.all.set(structure) \n
		Configures several settings for UL configured grant (combination of the other ...SPS:SASSignment:UL:... commands) , for
		the initial BWP. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Slot: int: Slot for sending the DCI that enables UL CG.
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Mcs: int: No parameter help available
			- Start_Symbol: int: No parameter help available
			- Number_Symbol: int: No parameter help available
			- Mapping: enums.Mapping: Type of PUSCH mapping
			- Offset: int: Slot offset k2 for the PUSCH"""
		__meta_args_list = [
			ArgStruct.scalar_int('Slot'),
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_int('Mcs'),
			ArgStruct.scalar_int('Start_Symbol'),
			ArgStruct.scalar_int('Number_Symbol'),
			ArgStruct.scalar_enum('Mapping', enums.Mapping),
			ArgStruct.scalar_int('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Slot: int = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Mcs: int = None
			self.Start_Symbol: int = None
			self.Number_Symbol: int = None
			self.Mapping: enums.Mapping = None
			self.Offset: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.all.get(cell_name = 'abc') \n
		Configures several settings for UL configured grant (combination of the other ...SPS:SASSignment:UL:... commands) , for
		the initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:ALL? {param}', self.__class__.GetStruct())
