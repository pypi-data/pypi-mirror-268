from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IdCls:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:BWP<bwpid>:ID \n
		Snippet: value: int = driver.sense.signaling.nradio.cell.bwp.id.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: bwp_id: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:ID? {param}')
		return Conversions.str_to_int(response)
