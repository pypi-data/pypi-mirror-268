from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PfOffsetCls:
	"""PfOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pfOffset", core, parent)

	def set(self, cell_name: str, frame: enums.Frame, offset: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PCYCle:PFOFfset \n
		Snippet: driver.configure.signaling.nradio.cell.pcycle.pfOffset.set(cell_name = 'abc', frame = enums.Frame.T16, offset = 1) \n
		Configures the field 'nAndPagingFrameOffset', used by the UE as input for the calculation of paging radio frame and
		paging occasion. \n
			:param cell_name: No help available
			:param frame: T1T: 1 T2 | T4 | T8 | T16: 1/2, 1/4, 1/8, 1/16
			:param offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('frame', frame, DataType.Enum, enums.Frame), ArgSingle('offset', offset, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PCYCle:PFOFfset {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Frame: enums.Frame: T1T: 1 T2 | T4 | T8 | T16: 1/2, 1/4, 1/8, 1/16
			- Offset: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Frame', enums.Frame),
			ArgStruct.scalar_int('Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frame: enums.Frame = None
			self.Offset: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PCYCle:PFOFfset \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.pcycle.pfOffset.get(cell_name = 'abc') \n
		Configures the field 'nAndPagingFrameOffset', used by the UE as input for the calculation of paging radio frame and
		paging occasion. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:PCYCle:PFOFfset? {param}', self.__class__.GetStruct())
