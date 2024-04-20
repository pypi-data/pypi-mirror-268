from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfChannelCls:
	"""RfChannel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfChannel", core, parent)

	def delete(self, cell_name: str) -> None:
		"""SCPI: DELete:SIGNaling:RFCHannel \n
		Snippet: driver.signaling.rfChannel.delete(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'DELete:SIGNaling:RFCHannel {param}')

	def reset(self) -> None:
		"""SCPI: RESet:SIGNaling:RFCHannel \n
		Snippet: driver.signaling.rfChannel.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'RESet:SIGNaling:RFCHannel')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: RESet:SIGNaling:RFCHannel \n
		Snippet: driver.signaling.rfChannel.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'RESet:SIGNaling:RFCHannel', opc_timeout_ms)
