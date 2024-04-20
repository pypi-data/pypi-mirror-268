from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CnetworkCls:
	"""Cnetwork commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnetwork", core, parent)

	def set(self) -> None:
		"""SCPI: RESTart:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.restart.signaling.topology.cnetwork.set() \n
		Restarts the core network in live mode and resets the DUT states to Idle. Afterwards, you are back in live mode.
		The cells still exist and are switched off. \n
		"""
		self._core.io.write(f'RESTart:SIGNaling:TOPology:CNETwork')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: RESTart:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.restart.signaling.topology.cnetwork.set_with_opc() \n
		Restarts the core network in live mode and resets the DUT states to Idle. Afterwards, you are back in live mode.
		The cells still exist and are switched off. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'RESTart:SIGNaling:TOPology:CNETwork', opc_timeout_ms)
