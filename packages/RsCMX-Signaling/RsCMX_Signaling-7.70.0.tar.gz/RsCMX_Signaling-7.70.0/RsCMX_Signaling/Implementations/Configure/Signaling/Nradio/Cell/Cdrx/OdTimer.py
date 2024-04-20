from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OdTimerCls:
	"""OdTimer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("odTimer", core, parent)

	def set(self, cell_name: str, timer: enums.OnDurationTimer) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:ODTimer \n
		Snippet: driver.configure.signaling.nradio.cell.cdrx.odTimer.set(cell_name = 'abc', timer = enums.OnDurationTimer.M1) \n
		Configures the 'drx-onDurationTimer'. \n
			:param cell_name: No help available
			:param timer: M1D to M31D: 1/32 ms to 31/32 ms M1 to M800: 1 ms to 800 ms M1K0 to M1K6: 1000 ms to 1600 ms
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('timer', timer, DataType.Enum, enums.OnDurationTimer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:ODTimer {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.OnDurationTimer:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:ODTimer \n
		Snippet: value: enums.OnDurationTimer = driver.configure.signaling.nradio.cell.cdrx.odTimer.get(cell_name = 'abc') \n
		Configures the 'drx-onDurationTimer'. \n
			:param cell_name: No help available
			:return: timer: M1D to M31D: 1/32 ms to 31/32 ms M1 to M800: 1 ms to 800 ms M1K0 to M1K6: 1000 ms to 1600 ms"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:ODTimer? {param}')
		return Conversions.str_to_scalar_enum(response, enums.OnDurationTimer)
