from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsZeroCls:
	"""SsZero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssZero", core, parent)

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CSSZero:SSZero \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.cssZero.ssZero.get(cell_name = 'abc') \n
		Queries the common search space number 0. \n
			:param cell_name: No help available
			:return: zero: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CSSZero:SSZero? {param}')
		return Conversions.str_to_int(response)
