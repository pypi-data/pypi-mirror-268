from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmrsPositionCls:
	"""DmrsPosition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrsPosition", core, parent)

	def set(self, cell_name: str, position: enums.SpsPosition) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:DMRSposition \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.dmrsPosition.set(cell_name = 'abc', position = enums.SpsPosition.POS0) \n
		Configures the signaled 'dmrs-AdditionalPosition' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:param position: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('position', position, DataType.Enum, enums.SpsPosition))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:DMRSposition {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.SpsPosition:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:DMRSposition \n
		Snippet: value: enums.SpsPosition = driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.dmrsPosition.get(cell_name = 'abc') \n
		Configures the signaled 'dmrs-AdditionalPosition' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: position: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:DMRSposition? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SpsPosition)
