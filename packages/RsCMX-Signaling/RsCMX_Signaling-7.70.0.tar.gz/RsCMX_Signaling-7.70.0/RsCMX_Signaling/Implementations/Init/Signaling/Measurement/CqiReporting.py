from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CqiReportingCls:
	"""CqiReporting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqiReporting", core, parent)

	def set(self) -> None:
		"""SCPI: INIT:SIGNaling:MEASurement:CQIReporting \n
		Snippet: driver.init.signaling.measurement.cqiReporting.set() \n
		Starts the measurement. The measurement enters the 'RUN' state. \n
		"""
		self._core.io.write(f'INIT:SIGNaling:MEASurement:CQIReporting')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INIT:SIGNaling:MEASurement:CQIReporting \n
		Snippet: driver.init.signaling.measurement.cqiReporting.set_with_opc() \n
		Starts the measurement. The measurement enters the 'RUN' state. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INIT:SIGNaling:MEASurement:CQIReporting', opc_timeout_ms)
