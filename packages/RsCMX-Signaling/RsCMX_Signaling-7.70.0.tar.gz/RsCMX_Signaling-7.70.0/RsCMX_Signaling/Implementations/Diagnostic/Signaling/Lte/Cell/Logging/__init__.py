from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoggingCls:
	"""Logging commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logging", core, parent)

	@property
	def mac(self):
		"""mac commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import MacCls
			self._mac = MacCls(self._core, self._cmd_group)
		return self._mac

	@property
	def rlc(self):
		"""rlc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlc'):
			from .Rlc import RlcCls
			self._rlc = RlcCls(self._core, self._cmd_group)
		return self._rlc

	@property
	def pdcp(self):
		"""pdcp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcp'):
			from .Pdcp import PdcpCls
			self._pdcp = PdcpCls(self._core, self._cmd_group)
		return self._pdcp

	def clone(self) -> 'LoggingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LoggingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
