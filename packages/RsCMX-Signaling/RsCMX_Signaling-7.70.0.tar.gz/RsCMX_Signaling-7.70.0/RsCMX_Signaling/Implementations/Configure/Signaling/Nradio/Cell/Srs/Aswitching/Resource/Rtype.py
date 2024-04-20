from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RtypeCls:
	"""Rtype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtype", core, parent)

	def set(self, cell_name: str, resource_no: int, period: int = None, offset: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RTYPe \n
		Snippet: driver.configure.signaling.nradio.cell.srs.aswitching.resource.rtype.set(cell_name = 'abc', resource_no = 1, period = 1, offset = 1) \n
		Configures the resource type for SRS resource <ResourceNo> for SRS antenna switching, for the initial BWP. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:param period: Periodicity of slots (SRS every nth slot)
			:param offset: Offset as number of slots. Must be smaller than the Period.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer), ArgSingle('period', period, DataType.Integer, None, is_optional=True), ArgSingle('offset', offset, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RTYPe {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Period: int: Periodicity of slots (SRS every nth slot)
			- Offset: int: Offset as number of slots. Must be smaller than the Period."""
		__meta_args_list = [
			ArgStruct.scalar_int('Period'),
			ArgStruct.scalar_int('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Period: int = None
			self.Offset: int = None

	def get(self, cell_name: str, resource_no: int) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RTYPe \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.srs.aswitching.resource.rtype.get(cell_name = 'abc', resource_no = 1) \n
		Configures the resource type for SRS resource <ResourceNo> for SRS antenna switching, for the initial BWP. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:SRS:ASWitching:RESource:RTYPe? {param}'.rstrip(), self.__class__.GetStruct())
