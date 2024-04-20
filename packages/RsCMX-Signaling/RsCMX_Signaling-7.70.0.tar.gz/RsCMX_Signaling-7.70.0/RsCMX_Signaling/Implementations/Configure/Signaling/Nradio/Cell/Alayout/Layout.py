from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LayoutCls:
	"""Layout commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layout", core, parent)

	def set(self, cell_name: str, antenna_layout: enums.AntennaLayout) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:ALAYout:LAYout \n
		Snippet: driver.configure.signaling.nradio.cell.alayout.layout.set(cell_name = 'abc', antenna_layout = enums.AntennaLayout.N121) \n
		Configures the layout of the CSI antenna port array. \n
			:param cell_name: No help available
			:param antenna_layout: TX2 for 1 or 2 CSI-RS antenna ports Nab for 2*a*b antenna ports, a=N1, b=N2
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('antenna_layout', antenna_layout, DataType.Enum, enums.AntennaLayout))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:ALAYout:LAYout {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.AntennaLayout:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:ALAYout:LAYout \n
		Snippet: value: enums.AntennaLayout = driver.configure.signaling.nradio.cell.alayout.layout.get(cell_name = 'abc') \n
		Configures the layout of the CSI antenna port array. \n
			:param cell_name: No help available
			:return: antenna_layout: TX2 for 1 or 2 CSI-RS antenna ports Nab for 2*a*b antenna ports, a=N1, b=N2"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:ALAYout:LAYout? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AntennaLayout)
