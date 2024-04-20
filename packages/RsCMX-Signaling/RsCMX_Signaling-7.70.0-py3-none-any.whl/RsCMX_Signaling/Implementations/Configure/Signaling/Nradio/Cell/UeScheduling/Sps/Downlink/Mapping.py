from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MappingCls:
	"""Mapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mapping", core, parent)

	def set(self, cell_name: str, mapping: enums.MappingI) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:MAPPing \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.downlink.mapping.set(cell_name = 'abc', mapping = enums.MappingI.INT) \n
		Selects whether interleaved or non-interleaved virtual RB to physical RB mapping is applied for the PDSCH, for DL SPS
		scheduling, for the initial BWP. \n
			:param cell_name: No help available
			:param mapping: Interleaved or non-interleaved
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mapping', mapping, DataType.Enum, enums.MappingI))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:MAPPing {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.MappingI:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:MAPPing \n
		Snippet: value: enums.MappingI = driver.configure.signaling.nradio.cell.ueScheduling.sps.downlink.mapping.get(cell_name = 'abc') \n
		Selects whether interleaved or non-interleaved virtual RB to physical RB mapping is applied for the PDSCH, for DL SPS
		scheduling, for the initial BWP. \n
			:param cell_name: No help available
			:return: mapping: Interleaved or non-interleaved"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:DL:MAPPing? {param}')
		return Conversions.str_to_scalar_enum(response, enums.MappingI)
