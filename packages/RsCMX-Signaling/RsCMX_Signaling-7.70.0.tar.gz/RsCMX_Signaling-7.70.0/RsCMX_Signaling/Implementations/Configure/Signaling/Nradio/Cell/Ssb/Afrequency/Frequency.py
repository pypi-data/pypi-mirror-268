from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:AFRequency:FREQuency \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.ssb.afrequency.frequency.get(cell_name = 'abc') \n
		Queries the center frequency of the SSB. \n
			:param cell_name: No help available
			:return: frequency: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SSB:AFRequency:FREQuency? {param}')
		return Conversions.str_to_float(response)
