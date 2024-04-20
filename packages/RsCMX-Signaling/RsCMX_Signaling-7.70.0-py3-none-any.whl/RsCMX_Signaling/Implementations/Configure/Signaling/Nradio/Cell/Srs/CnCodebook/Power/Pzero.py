from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PzeroCls:
	"""Pzero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pzero", core, parent)

	def set(self, cell_name: str, p_0: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:PZERo \n
		Snippet: driver.configure.signaling.nradio.cell.srs.cnCodebook.power.pzero.set(cell_name = 'abc', p_0 = 1) \n
		Sets the SRS power control parameter 'p0' for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
			:param p_0: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('p_0', p_0, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:PZERo {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:PZERo \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.srs.cnCodebook.power.pzero.get(cell_name = 'abc') \n
		Sets the SRS power control parameter 'p0' for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
			:return: p_0: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:PZERo? {param}')
		return Conversions.str_to_int(response)
