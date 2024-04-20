from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BearerCls:
	"""Bearer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bearer", core, parent)

	def delete(self, bearer_id: int) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:EPS:BEARer \n
		Snippet: driver.signaling.topology.eps.bearer.delete(bearer_id = 1) \n
		Establishes a dedicated bearer. \n
			:param bearer_id: ID of the dedicated bearer
		"""
		param = Conversions.decimal_value_to_str(bearer_id)
		self._core.io.write(f'DELete:SIGNaling:TOPology:EPS:BEARer {param}')
