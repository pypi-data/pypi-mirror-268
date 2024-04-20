from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeFrecoveryB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CMATrix:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.cmatrix.mode.set(cell_name = 'abc', mode = enums.ModeFrecoveryB.HADamard) \n
		Activates a channel matrix. \n
			:param cell_name: No help available
			:param mode: OFF: Without a fader in the signal path, IDENtity matrix. With a fader in the signal path, TGPP matrix. UDEFined: Matrix defined via another operating interface. TGPP: Matrix defined in 3GPP TS 38.101-4 annex B.1. HADamard: Hadamard matrix. IDENtity: Identity matrix.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeFrecoveryB))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CMATrix:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeFrecoveryB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CMATrix:MODE \n
		Snippet: value: enums.ModeFrecoveryB = driver.configure.signaling.nradio.cell.cmatrix.mode.get(cell_name = 'abc') \n
		Activates a channel matrix. \n
			:param cell_name: No help available
			:return: mode: OFF: Without a fader in the signal path, IDENtity matrix. With a fader in the signal path, TGPP matrix. UDEFined: Matrix defined via another operating interface. TGPP: Matrix defined in 3GPP TS 38.101-4 annex B.1. HADamard: Hadamard matrix. IDENtity: Identity matrix."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CMATrix:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeFrecoveryB)
