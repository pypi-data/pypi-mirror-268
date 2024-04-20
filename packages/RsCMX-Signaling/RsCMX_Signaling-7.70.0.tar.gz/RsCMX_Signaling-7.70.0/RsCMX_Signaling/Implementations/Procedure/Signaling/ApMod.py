from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApModCls:
	"""ApMod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apMod", core, parent)

	def set(self) -> None:
		"""SCPI: PROCedure:SIGNaling:APMod \n
		Snippet: driver.procedure.signaling.apMod.set() \n
		Applies all pending changes. \n
		"""
		self._core.io.write(f'PROCedure:SIGNaling:APMod')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: PROCedure:SIGNaling:APMod \n
		Snippet: driver.procedure.signaling.apMod.set_with_opc() \n
		Applies all pending changes. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'PROCedure:SIGNaling:APMod', opc_timeout_ms)
