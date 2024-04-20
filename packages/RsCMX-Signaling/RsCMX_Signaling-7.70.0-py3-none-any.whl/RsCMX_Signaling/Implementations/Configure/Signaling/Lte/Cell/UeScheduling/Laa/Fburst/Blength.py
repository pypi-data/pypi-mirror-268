from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlengthCls:
	"""Blength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blength", core, parent)

	def set(self, cell_name: str, burst_length: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:BLENgth \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.blength.set(cell_name = 'abc', burst_length = 1) \n
		Configures the length of fixed bursts (number of subframes) . \n
			:param cell_name: No help available
			:param burst_length: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('burst_length', burst_length, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:BLENgth {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:BLENgth \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.blength.get(cell_name = 'abc') \n
		Configures the length of fixed bursts (number of subframes) . \n
			:param cell_name: No help available
			:return: burst_length: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:BLENgth? {param}')
		return Conversions.str_to_int(response)
