from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PositionCls:
	"""Position commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def set(self, cell_name: str, position: enums.MtxPosition) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:DL:MTB:POSition \n
		Snippet: driver.configure.signaling.nradio.cell.dmrs.downlink.mtb.position.set(cell_name = 'abc', position = enums.MtxPosition.P0) \n
		Defines parameter 'dmrs-AdditionalPosition' for PDSCH, mapping type B, initial BWP. \n
			:param cell_name: No help available
			:param position: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('position', position, DataType.Enum, enums.MtxPosition))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:DL:MTB:POSition {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.MtxPosition:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:DL:MTB:POSition \n
		Snippet: value: enums.MtxPosition = driver.configure.signaling.nradio.cell.dmrs.downlink.mtb.position.get(cell_name = 'abc') \n
		Defines parameter 'dmrs-AdditionalPosition' for PDSCH, mapping type B, initial BWP. \n
			:param cell_name: No help available
			:return: position: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:DL:MTB:POSition? {param}')
		return Conversions.str_to_scalar_enum(response, enums.MtxPosition)
