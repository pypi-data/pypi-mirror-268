from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QuantityCls:
	"""Quantity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("quantity", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Quantity:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:REPort:QUANtity \n
		Snippet: value: enums.Quantity = driver.sense.signaling.nradio.cell.bwp.cqiReporting.report.quantity.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: quantity: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:REPort:QUANtity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Quantity)
