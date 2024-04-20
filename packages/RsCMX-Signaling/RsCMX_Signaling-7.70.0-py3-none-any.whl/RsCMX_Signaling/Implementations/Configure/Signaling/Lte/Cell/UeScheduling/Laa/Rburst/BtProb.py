from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BtProbCls:
	"""BtProb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btProb", core, parent)

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:BTPRob \n
		Snippet: value: float = driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.btProb.get(cell_name = 'abc') \n
		Queries the probability for the decision of the random transmission procedure, whether a random burst is transmitted or
		whether muting is applied for the burst duration. \n
			:param cell_name: No help available
			:return: ratio: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:BTPRob? {param}')
		return Conversions.str_to_float(response)
