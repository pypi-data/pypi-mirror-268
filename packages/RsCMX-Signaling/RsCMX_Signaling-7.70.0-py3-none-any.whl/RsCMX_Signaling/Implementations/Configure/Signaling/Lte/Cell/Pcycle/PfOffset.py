from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PfOffsetCls:
	"""PfOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pfOffset", core, parent)

	def set(self, cell_name: str, frames_offset: enums.FramesOffset) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:PCYCle:PFOFfset \n
		Snippet: driver.configure.signaling.lte.cell.pcycle.pfOffset.set(cell_name = 'abc', frames_offset = enums.FramesOffset.T16) \n
		Configures the field 'nB', used by the UE as input for the calculation of paging radio frame and paging occasion. \n
			:param cell_name: No help available
			:param frames_offset: T4T, T2T, T1T: 4, 2, 1 T2 | T4 | T8 | T16 | T32: 1/2, 1/4, 1/8, 1/16, 1/32
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('frames_offset', frames_offset, DataType.Enum, enums.FramesOffset))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:PCYCle:PFOFfset {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FramesOffset:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:PCYCle:PFOFfset \n
		Snippet: value: enums.FramesOffset = driver.configure.signaling.lte.cell.pcycle.pfOffset.get(cell_name = 'abc') \n
		Configures the field 'nB', used by the UE as input for the calculation of paging radio frame and paging occasion. \n
			:param cell_name: No help available
			:return: frames_offset: T4T, T2T, T1T: 4, 2, 1 T2 | T4 | T8 | T16 | T32: 1/2, 1/4, 1/8, 1/16, 1/32"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:PCYCle:PFOFfset? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FramesOffset)
