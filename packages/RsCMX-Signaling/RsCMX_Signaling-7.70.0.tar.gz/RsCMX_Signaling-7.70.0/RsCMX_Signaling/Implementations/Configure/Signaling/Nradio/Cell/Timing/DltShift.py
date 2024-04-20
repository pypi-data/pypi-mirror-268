from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DltShiftCls:
	"""DltShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dltShift", core, parent)

	def set(self, cell_name: str, delta: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TIMing:DLTShift \n
		Snippet: driver.configure.signaling.nradio.cell.timing.dltShift.set(cell_name = 'abc', delta = 1) \n
		Defines a DL time offset for a cell, after switching it on. \n
			:param cell_name: No help available
			:param delta: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('delta', delta, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:TIMing:DLTShift {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TIMing:DLTShift \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.timing.dltShift.get(cell_name = 'abc') \n
		Defines a DL time offset for a cell, after switching it on. \n
			:param cell_name: No help available
			:return: delta: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:TIMing:DLTShift? {param}')
		return Conversions.str_to_int(response)
