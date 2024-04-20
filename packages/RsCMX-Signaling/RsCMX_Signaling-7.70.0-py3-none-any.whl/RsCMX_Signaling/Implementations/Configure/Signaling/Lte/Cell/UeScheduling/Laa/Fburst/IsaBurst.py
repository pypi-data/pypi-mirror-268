from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsaBurstCls:
	"""IsaBurst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isaBurst", core, parent)

	def set(self, cell_name: str, initial_sf_alloc: enums.InitialSfAlloc) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ISABurst \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.isaBurst.set(cell_name = 'abc', initial_sf_alloc = enums.InitialSfAlloc.S0) \n
		Selects the first allocated symbol for the first subframe of a fixed burst. \n
			:param cell_name: No help available
			:param initial_sf_alloc: Symbol 0 (full allocation of subframe) or symbol 7 (second slot of subframe)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('initial_sf_alloc', initial_sf_alloc, DataType.Enum, enums.InitialSfAlloc))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ISABurst {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.InitialSfAlloc:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ISABurst \n
		Snippet: value: enums.InitialSfAlloc = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.isaBurst.get(cell_name = 'abc') \n
		Selects the first allocated symbol for the first subframe of a fixed burst. \n
			:param cell_name: No help available
			:return: initial_sf_alloc: Symbol 0 (full allocation of subframe) or symbol 7 (second slot of subframe)"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:ISABurst? {param}')
		return Conversions.str_to_scalar_enum(response, enums.InitialSfAlloc)
