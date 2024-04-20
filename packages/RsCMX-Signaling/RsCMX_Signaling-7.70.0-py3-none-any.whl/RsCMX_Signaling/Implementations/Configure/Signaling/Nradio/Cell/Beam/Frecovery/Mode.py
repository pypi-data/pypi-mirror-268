from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeFrecovery) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.beam.frecovery.mode.set(cell_name = 'abc', mode = enums.ModeFrecovery.AUTO) \n
		Selects a mode for configuration of the candidate list for beam failure recovery. \n
			:param cell_name: No help available
			:param mode:
				- OFF: No candidate list, no recovery.
				- AUTO: The active beam is the only candidate.
				- UDEFined: Configuration via [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:SSB and [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:CSIRs."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeFrecovery))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeFrecovery:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE \n
		Snippet: value: enums.ModeFrecovery = driver.configure.signaling.nradio.cell.beam.frecovery.mode.get(cell_name = 'abc') \n
		Selects a mode for configuration of the candidate list for beam failure recovery. \n
			:param cell_name: No help available
			:return: mode:
				- OFF: No candidate list, no recovery.
				- AUTO: The active beam is the only candidate.
				- UDEFined: Configuration via [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:SSB and [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:CSIRs."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeFrecovery)
