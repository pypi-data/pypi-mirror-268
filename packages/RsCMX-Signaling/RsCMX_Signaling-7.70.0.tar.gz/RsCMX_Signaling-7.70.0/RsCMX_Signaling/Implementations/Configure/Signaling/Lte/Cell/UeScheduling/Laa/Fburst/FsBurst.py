from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FsBurstCls:
	"""FsBurst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsBurst", core, parent)

	def set(self, cell_name: str, first_subframe: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:FSBurst \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.fsBurst.set(cell_name = 'abc', first_subframe = 1) \n
		Selects the first subframe used for fixed bursts. Zero refers to subframe 0 in system frame 0 (SFN 0) . \n
			:param cell_name: No help available
			:param first_subframe: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('first_subframe', first_subframe, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:FSBurst {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:FSBurst \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.fsBurst.get(cell_name = 'abc') \n
		Selects the first subframe used for fixed bursts. Zero refers to subframe 0 in system frame 0 (SFN 0) . \n
			:param cell_name: No help available
			:return: first_subframe: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:FSBurst? {param}')
		return Conversions.str_to_int(response)
