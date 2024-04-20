from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FmodeCls:
	"""Fmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeBfollow) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FOLLowing:FMODe \n
		Snippet: driver.configure.signaling.nradio.cell.beam.following.fmode.set(cell_name = 'abc', mode = enums.ModeBfollow.AUTO) \n
		Selects a mode for the DL beam following. \n
			:param cell_name: No help available
			:param mode: OFF: No beam following AUTO: Beam selection based on UE measurement reports BLOCk: Beamlock configuration via [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FOLLowing:BLOCk
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeBfollow))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FOLLowing:FMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeBfollow:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FOLLowing:FMODe \n
		Snippet: value: enums.ModeBfollow = driver.configure.signaling.nradio.cell.beam.following.fmode.get(cell_name = 'abc') \n
		Selects a mode for the DL beam following. \n
			:param cell_name: No help available
			:return: mode: OFF: No beam following AUTO: Beam selection based on UE measurement reports BLOCk: Beamlock configuration via [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FOLLowing:BLOCk"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FOLLowing:FMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeBfollow)
