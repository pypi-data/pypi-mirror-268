from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmodeCls:
	"""Smode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeE) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SMODe \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.smode.set(cell_name = 'abc', mode = enums.ModeE.CPRI) \n
		No command help available \n
			:param cell_name: No help available
			:param mode: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeE))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeE:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SMODe \n
		Snippet: value: enums.ModeE = driver.configure.signaling.lte.cell.ueScheduling.smode.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: mode: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeE)
