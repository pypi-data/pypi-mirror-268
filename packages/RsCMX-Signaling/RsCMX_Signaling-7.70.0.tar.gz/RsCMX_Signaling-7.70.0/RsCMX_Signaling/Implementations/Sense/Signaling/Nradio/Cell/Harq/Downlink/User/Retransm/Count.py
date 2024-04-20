from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, cell_name: str) -> int:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm:COUNt \n
		Snippet: value: int = driver.sense.signaling.nradio.cell.harq.downlink.user.retransm.count.get(cell_name = 'abc') \n
		Queries the number of DL retransmissions for the initial BWP. \n
			:param cell_name: No help available
			:return: retransmissions: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm:COUNt? {param}')
		return Conversions.str_to_int(response)
