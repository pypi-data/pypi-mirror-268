from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PopFrameCls:
	"""PopFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("popFrame", core, parent)

	def set(self, cell_name: str, occasions: enums.AntNoPorts) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PCYCle:POPFrame \n
		Snippet: driver.configure.signaling.nradio.cell.pcycle.popFrame.set(cell_name = 'abc', occasions = enums.AntNoPorts.P1) \n
		Configures the field 'ns', indicating the number of paging occasions per paging frame. \n
			:param cell_name: No help available
			:param occasions: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('occasions', occasions, DataType.Enum, enums.AntNoPorts))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PCYCle:POPFrame {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.AntNoPorts:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PCYCle:POPFrame \n
		Snippet: value: enums.AntNoPorts = driver.configure.signaling.nradio.cell.pcycle.popFrame.get(cell_name = 'abc') \n
		Configures the field 'ns', indicating the number of paging occasions per paging frame. \n
			:param cell_name: No help available
			:return: occasions: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PCYCle:POPFrame? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AntNoPorts)
