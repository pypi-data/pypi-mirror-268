from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlphaCls:
	"""Alpha commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpha", core, parent)

	def set(self, cell_name: str, alpha: enums.Alpha) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:ALPHa \n
		Snippet: driver.configure.signaling.nradio.cell.srs.cnCodebook.power.alpha.set(cell_name = 'abc', alpha = enums.Alpha.A00) \n
		Sets the SRS power control parameter 'alpha' for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
			:param alpha: Axy means x.y.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('alpha', alpha, DataType.Enum, enums.Alpha))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:ALPHa {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Alpha:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:ALPHa \n
		Snippet: value: enums.Alpha = driver.configure.signaling.nradio.cell.srs.cnCodebook.power.alpha.get(cell_name = 'abc') \n
		Sets the SRS power control parameter 'alpha' for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
			:return: alpha: Axy means x.y."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:POWer:ALPHa? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Alpha)
