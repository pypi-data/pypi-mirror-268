from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PiBurstCls:
	"""PiBurst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("piBurst", core, parent)

	def set(self, cell_name: str, beam_config_mode: enums.BeamConfigMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:BEAM:PIBurst \n
		Snippet: driver.configure.signaling.nradio.cell.ssb.beam.piBurst.set(cell_name = 'abc', beam_config_mode = enums.BeamConfigMode.ALL) \n
		Selects a mode for configuration of the SS-block positions. \n
			:param cell_name: No help available
			:param beam_config_mode: AUTO: Use only position 1 (bitmap 0100...) . ALL: Use all possible positions (bitmap 1111...) . UDEFined: See [CONFigure:]SIGNaling:NRADio:CELL:SSB:BEAM:MODel.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('beam_config_mode', beam_config_mode, DataType.Enum, enums.BeamConfigMode))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SSB:BEAM:PIBurst {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.BeamConfigMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:BEAM:PIBurst \n
		Snippet: value: enums.BeamConfigMode = driver.configure.signaling.nradio.cell.ssb.beam.piBurst.get(cell_name = 'abc') \n
		Selects a mode for configuration of the SS-block positions. \n
			:param cell_name: No help available
			:return: beam_config_mode: AUTO: Use only position 1 (bitmap 0100...) . ALL: Use all possible positions (bitmap 1111...) . UDEFined: See [CONFigure:]SIGNaling:NRADio:CELL:SSB:BEAM:MODel."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SSB:BEAM:PIBurst? {param}')
		return Conversions.str_to_scalar_enum(response, enums.BeamConfigMode)
