from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlOffsetCls:
	"""RlOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlOffset", core, parent)

	def set(self, cell_name: str, ref_level_offset: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:AUTO:RLOFfset \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.auto.rlOffset.set(cell_name = 'abc', ref_level_offset = 1.0) \n
		Sets the reference level offset for automatic configuration of expected UL power. \n
			:param cell_name: No help available
			:param ref_level_offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ref_level_offset', ref_level_offset, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:AUTO:RLOFfset {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:AUTO:RLOFfset \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.power.uplink.auto.rlOffset.get(cell_name = 'abc') \n
		Sets the reference level offset for automatic configuration of expected UL power. \n
			:param cell_name: No help available
			:return: ref_level_offset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:AUTO:RLOFfset? {param}')
		return Conversions.str_to_float(response)
