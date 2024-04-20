from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbgSizeCls:
	"""RbgSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbgSize", core, parent)

	def set(self, cell_name: str, rgb_size: enums.RgbSize) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:RBGSize \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.downlink.rbgSize.set(cell_name = 'abc', rgb_size = enums.RgbSize.CON1) \n
		Configures the signaled 'rbg-Size' for DL SPS scheduling, for the initial BWP. \n
			:param cell_name: No help available
			:param rgb_size: Config 1 or 2
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('rgb_size', rgb_size, DataType.Enum, enums.RgbSize))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:RBGSize {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.RgbSize:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:RBGSize \n
		Snippet: value: enums.RgbSize = driver.configure.signaling.nradio.cell.ueScheduling.sps.downlink.rbgSize.get(cell_name = 'abc') \n
		Configures the signaled 'rbg-Size' for DL SPS scheduling, for the initial BWP. \n
			:param cell_name: No help available
			:return: rgb_size: Config 1 or 2"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:RBGSize? {param}')
		return Conversions.str_to_scalar_enum(response, enums.RgbSize)
