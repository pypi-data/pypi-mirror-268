from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResourceCls:
	"""Resource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resource", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Resource_No: int: No parameter help available
			- Resource_Id: int: No parameter help available
			- No_Srs_Ports: enums.AntNoPorts: Optional setting parameter. Number of antenna ports for SRS transmissions
			- Fd_Position: int: Optional setting parameter. Frequency domain position
			- Fd_Shift: int: Optional setting parameter. Frequency domain shift
			- Sequence_Id: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Resource_No'),
			ArgStruct.scalar_int('Resource_Id'),
			ArgStruct.scalar_enum_optional('No_Srs_Ports', enums.AntNoPorts),
			ArgStruct.scalar_int_optional('Fd_Position'),
			ArgStruct.scalar_int_optional('Fd_Shift'),
			ArgStruct.scalar_int_optional('Sequence_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Resource_No: int = None
			self.Resource_Id: int = None
			self.No_Srs_Ports: enums.AntNoPorts = None
			self.Fd_Position: int = None
			self.Fd_Shift: int = None
			self.Sequence_Id: int = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RESource \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.srs.aswitching.resource.resource.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Resource_No: int = 1 \n
		structure.Resource_Id: int = 1 \n
		structure.No_Srs_Ports: enums.AntNoPorts = enums.AntNoPorts.P1 \n
		structure.Fd_Position: int = 1 \n
		structure.Fd_Shift: int = 1 \n
		structure.Sequence_Id: int = 1 \n
		driver.configure.signaling.nradio.cell.srs.aswitching.resource.resource.set(structure) \n
		Configures the SRS resource <ResourceNo> for SRS antenna switching, for the initial BWP. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RESource', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Resource_Id: int: No parameter help available
			- No_Srs_Ports: enums.AntNoPorts: Number of antenna ports for SRS transmissions
			- Fd_Position: int: Frequency domain position
			- Fd_Shift: int: Frequency domain shift
			- Sequence_Id: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Resource_Id'),
			ArgStruct.scalar_enum('No_Srs_Ports', enums.AntNoPorts),
			ArgStruct.scalar_int('Fd_Position'),
			ArgStruct.scalar_int('Fd_Shift'),
			ArgStruct.scalar_int('Sequence_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Resource_Id: int = None
			self.No_Srs_Ports: enums.AntNoPorts = None
			self.Fd_Position: int = None
			self.Fd_Shift: int = None
			self.Sequence_Id: int = None

	def get(self, cell_name: str, resource_no: int) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RESource \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.srs.aswitching.resource.resource.get(cell_name = 'abc', resource_no = 1) \n
		Configures the SRS resource <ResourceNo> for SRS antenna switching, for the initial BWP. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RESource? {param}'.rstrip(), self.__class__.GetStruct())
