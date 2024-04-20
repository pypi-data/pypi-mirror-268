from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NasCls:
	"""Nas commands group definition. 10 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nas", core, parent)

	@property
	def auth(self):
		"""auth commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_auth'):
			from .Auth import AuthCls
			self._auth = AuthCls(self._core, self._cmd_group)
		return self._auth

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_security'):
			from .Security import SecurityCls
			self._security = SecurityCls(self._core, self._cmd_group)
		return self._security

	@property
	def tlv(self):
		"""tlv commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tlv'):
			from .Tlv import TlvCls
			self._tlv = TlvCls(self._core, self._cmd_group)
		return self._tlv

	def clone(self) -> 'NasCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NasCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
