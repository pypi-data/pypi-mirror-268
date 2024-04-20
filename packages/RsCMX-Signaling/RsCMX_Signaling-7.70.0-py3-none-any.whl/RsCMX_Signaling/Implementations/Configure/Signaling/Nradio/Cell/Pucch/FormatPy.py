from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, cell_name: str, format_py: enums.CellPucchFormatPy) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUCCh:FORMat \n
		Snippet: driver.configure.signaling.nradio.cell.pucch.formatPy.set(cell_name = 'abc', format_py = enums.CellPucchFormatPy.F0) \n
		Selects the PUCCH format for the initial BWP. \n
			:param cell_name: No help available
			:param format_py: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('format_py', format_py, DataType.Enum, enums.CellPucchFormatPy))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUCCh:FORMat {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.CellPucchFormatPy:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUCCh:FORMat \n
		Snippet: value: enums.CellPucchFormatPy = driver.configure.signaling.nradio.cell.pucch.formatPy.get(cell_name = 'abc') \n
		Selects the PUCCH format for the initial BWP. \n
			:param cell_name: No help available
			:return: format_py: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUCCh:FORMat? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CellPucchFormatPy)
