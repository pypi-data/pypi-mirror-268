from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AsnCls:
	"""Asn commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asn", core, parent)

	@property
	def mib(self):
		"""mib commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mib'):
			from .Mib import MibCls
			self._mib = MibCls(self._core, self._cmd_group)
		return self._mib

	@property
	def sib1(self):
		"""sib1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sib1'):
			from .Sib1 import Sib1Cls
			self._sib1 = Sib1Cls(self._core, self._cmd_group)
		return self._sib1

	def clone(self) -> 'AsnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AsnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
