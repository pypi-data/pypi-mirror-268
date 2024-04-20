from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpsProbCls:
	"""IpsProb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipsProb", core, parent)

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:IPSProb \n
		Snippet: value: float = driver.configure.signaling.lte.cell.ueScheduling.laa.rburst.ipsProb.get(cell_name = 'abc') \n
		Queries the probability for the decision of the random transmission procedure, whether the first subframe of a random
		burst has a partial allocation (instead of a full allocation) . \n
			:param cell_name: No help available
			:return: ratio: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RBURst:IPSProb? {param}')
		return Conversions.str_to_float(response)
