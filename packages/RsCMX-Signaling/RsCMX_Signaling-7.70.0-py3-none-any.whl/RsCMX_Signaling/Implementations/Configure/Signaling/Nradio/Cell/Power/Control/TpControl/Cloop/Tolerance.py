from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ToleranceCls:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, cell_name: str, tolerance: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:CLOop:TOLerance \n
		Snippet: driver.configure.signaling.nradio.cell.power.control.tpControl.cloop.tolerance.set(cell_name = 'abc', tolerance = 1.0) \n
		Defines the tolerance for closed-loop power control for the initial BWP. \n
			:param cell_name: No help available
			:param tolerance: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('tolerance', tolerance, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:CLOop:TOLerance {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:CLOop:TOLerance \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.power.control.tpControl.cloop.tolerance.get(cell_name = 'abc') \n
		Defines the tolerance for closed-loop power control for the initial BWP. \n
			:param cell_name: No help available
			:return: tolerance: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:CLOop:TOLerance? {param}')
		return Conversions.str_to_float(response)
