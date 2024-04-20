from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnRatioCls:
	"""SnRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snRatio", core, parent)

	def set(self, cell_name: str, ratio: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:AWGN:SNRatio \n
		Snippet: driver.configure.signaling.awgn.snRatio.set(cell_name = 'abc', ratio = 1.0) \n
		Specifies the signal to noise ratio for AWGN insertion. \n
			:param cell_name: No help available
			:param ratio: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ratio', ratio, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:AWGN:SNRatio {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:AWGN:SNRatio \n
		Snippet: value: float = driver.configure.signaling.awgn.snRatio.get(cell_name = 'abc') \n
		Specifies the signal to noise ratio for AWGN insertion. \n
			:param cell_name: No help available
			:return: ratio: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:AWGN:SNRatio? {param}')
		return Conversions.str_to_float(response)
