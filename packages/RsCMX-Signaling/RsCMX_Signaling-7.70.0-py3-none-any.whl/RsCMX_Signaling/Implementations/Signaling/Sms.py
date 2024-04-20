from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmsCls:
	"""Sms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sms", core, parent)

	def clear(self) -> None:
		"""SCPI: CLEar:SIGNaling:SMS \n
		Snippet: driver.signaling.sms.clear() \n
		Clears information about received mobile-originated short messages. \n
		"""
		self._core.io.write(f'CLEar:SIGNaling:SMS')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CLEar:SIGNaling:SMS \n
		Snippet: driver.signaling.sms.clear_with_opc() \n
		Clears information about received mobile-originated short messages. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CLEar:SIGNaling:SMS', opc_timeout_ms)
