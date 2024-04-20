from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CnetworkCls:
	"""Cnetwork commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnetwork", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def delete(self) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.signaling.topology.cnetwork.delete() \n
		Deletes the core network. \n
		"""
		self._core.io.write(f'DELete:SIGNaling:TOPology:CNETwork')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DELete:SIGNaling:TOPology:CNETwork \n
		Snippet: driver.signaling.topology.cnetwork.delete_with_opc() \n
		Deletes the core network. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCMX_Signaling.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DELete:SIGNaling:TOPology:CNETwork', opc_timeout_ms)

	def clone(self) -> 'CnetworkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CnetworkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
