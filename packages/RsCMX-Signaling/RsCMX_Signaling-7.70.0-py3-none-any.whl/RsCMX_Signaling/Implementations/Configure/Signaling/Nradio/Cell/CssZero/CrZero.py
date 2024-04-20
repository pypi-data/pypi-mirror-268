from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrZeroCls:
	"""CrZero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crZero", core, parent)

	def set(self, cell_name: str, zero: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CSSZero:CRZero \n
		Snippet: driver.configure.signaling.nradio.cell.cssZero.crZero.set(cell_name = 'abc', zero = 1) \n
		Specifies the common control resource set (CORESET) number 0. \n
			:param cell_name: No help available
			:param zero: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('zero', zero, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CSSZero:CRZero {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CSSZero:CRZero \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.cssZero.crZero.get(cell_name = 'abc') \n
		Specifies the common control resource set (CORESET) number 0. \n
			:param cell_name: No help available
			:return: zero: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CSSZero:CRZero? {param}')
		return Conversions.str_to_int(response)
