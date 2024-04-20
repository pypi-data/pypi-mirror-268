from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserCls:
	"""User commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	def set_retransm(self, cell_name: str) -> None:
		"""SCPI: ADD:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm \n
		Snippet: driver.add.signaling.nradio.cell.harq.downlink.user.set_retransm(cell_name = 'abc') \n
		Adds a retransmission to the retransmission configuration for user-defined DL HARQ, for the initial BWP. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'ADD:SIGNaling:NRADio:CELL:HARQ:DL:USER:RETRansm {param}')
