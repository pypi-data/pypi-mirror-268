from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResourceCls:
	"""Resource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resource", core, parent)

	def delete(self, cell_name: str, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:RESource \n
		Snippet: driver.signaling.nradio.cell.bwp.srs.cnCodebook.resource.delete(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Removes an SRS resource from the resource set for periodic SRS, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:RESource {param}')
