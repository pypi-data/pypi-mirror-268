from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import enums
from .......... import repcap


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
			- Mcs_Table: enums.McsTableB: Optional setting parameter. 256QAM, 64QAM low SE, 64QAM
			- Alevel: enums.Level: Optional setting parameter. Aggregation level
			- Search_Space_Id: int: No parameter help available
			- Resource_Allocation_Type: enums.ResourceAllocationType: No parameter help available
			- Rgb_Size: enums.RgbSize: Optional setting parameter. Config 1 or 2
			- No_Harq: int: Optional setting parameter. Signaled 'nrofHARQ-Processes'
			- Mapping: enums.MappingI: Optional setting parameter. Interleaved or non-interleaved virtual RB to physical RB mapping
			- Padding: enums.SpsPadding: Optional setting parameter. No DL padding or with DL padding"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int_optional('Periodicity'),
			ArgStruct.scalar_enum_optional('Mcs_Table', enums.McsTableB),
			ArgStruct.scalar_enum_optional('Alevel', enums.Level),
			ArgStruct.scalar_int_optional('Search_Space_Id'),
			ArgStruct.scalar_enum_optional('Resource_Allocation_Type', enums.ResourceAllocationType),
			ArgStruct.scalar_enum_optional('Rgb_Size', enums.RgbSize),
			ArgStruct.scalar_int_optional('No_Harq'),
			ArgStruct.scalar_enum_optional('Mapping', enums.MappingI),
			ArgStruct.scalar_enum_optional('Padding', enums.SpsPadding)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Periodicity: int = None
			self.Mcs_Table: enums.McsTableB = None
			self.Alevel: enums.Level = None
			self.Search_Space_Id: int = None
			self.Resource_Allocation_Type: enums.ResourceAllocationType = None
			self.Rgb_Size: enums.RgbSize = None
			self.No_Harq: int = None
			self.Mapping: enums.MappingI = None
			self.Padding: enums.SpsPadding = None

	def set(self, structure: SetStruct, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:DL:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Periodicity: int = 1 \n
		structure.Mcs_Table: enums.McsTableB = enums.McsTableB.L64 \n
		structure.Alevel: enums.Level = enums.Level.AL1 \n
		structure.Search_Space_Id: int = 1 \n
		structure.Resource_Allocation_Type: enums.ResourceAllocationType = enums.ResourceAllocationType.DSWich \n
		structure.Rgb_Size: enums.RgbSize = enums.RgbSize.CON1 \n
		structure.No_Harq: int = 1 \n
		structure.Mapping: enums.MappingI = enums.MappingI.INT \n
		structure.Padding: enums.SpsPadding = enums.SpsPadding.ALLZero \n
		driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.all.set(structure, bwParts = repcap.BwParts.Default) \n
		Configures several settings for SPS DL scheduling (combination of the other ...SPS:DL:... commands) , for BWP <bb>. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:DL:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Periodicity: int: No parameter help available
			- Mcs_Table: enums.McsTableB: 256QAM, 64QAM low SE, 64QAM
			- Alevel: enums.Level: Aggregation level
			- Search_Space_Id: int: No parameter help available
			- Resource_Allocation_Type: enums.ResourceAllocationType: No parameter help available
			- Rgb_Size: enums.RgbSize: Config 1 or 2
			- No_Harq: int: Signaled 'nrofHARQ-Processes'
			- Mapping: enums.MappingI: Interleaved or non-interleaved virtual RB to physical RB mapping
			- Padding: enums.SpsPadding: No DL padding or with DL padding"""
		__meta_args_list = [
			ArgStruct.scalar_int('Periodicity'),
			ArgStruct.scalar_enum('Mcs_Table', enums.McsTableB),
			ArgStruct.scalar_enum('Alevel', enums.Level),
			ArgStruct.scalar_int('Search_Space_Id'),
			ArgStruct.scalar_enum('Resource_Allocation_Type', enums.ResourceAllocationType),
			ArgStruct.scalar_enum('Rgb_Size', enums.RgbSize),
			ArgStruct.scalar_int('No_Harq'),
			ArgStruct.scalar_enum('Mapping', enums.MappingI),
			ArgStruct.scalar_enum('Padding', enums.SpsPadding)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Periodicity: int = None
			self.Mcs_Table: enums.McsTableB = None
			self.Alevel: enums.Level = None
			self.Search_Space_Id: int = None
			self.Resource_Allocation_Type: enums.ResourceAllocationType = None
			self.Rgb_Size: enums.RgbSize = None
			self.No_Harq: int = None
			self.Mapping: enums.MappingI = None
			self.Padding: enums.SpsPadding = None

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:DL:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.all.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures several settings for SPS DL scheduling (combination of the other ...SPS:DL:... commands) , for BWP <bb>. \n
			:param cell_name: Type 0, type 1, dynamic switch
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:DL:ALL? {param}', self.__class__.GetStruct())
