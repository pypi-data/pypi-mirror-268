from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NbBeamsCls:
	"""NbBeams commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbBeams", core, parent)

	def set(self, cell_name: str, number: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAMs:NBBeams \n
		Snippet: driver.configure.signaling.nradio.cell.beams.nbBeams.set(cell_name = 'abc', number = 1) \n
		Creates a <Number> of NZP CSI-RS beams within the active beam. \n
			:param cell_name: No help available
			:param number: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('number', number, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAMs:NBBeams {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAMs:NBBeams \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.beams.nbBeams.get(cell_name = 'abc') \n
		Creates a <Number> of NZP CSI-RS beams within the active beam. \n
			:param cell_name: No help available
			:return: number: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BEAMs:NBBeams? {param}')
		return Conversions.str_to_int(response)
