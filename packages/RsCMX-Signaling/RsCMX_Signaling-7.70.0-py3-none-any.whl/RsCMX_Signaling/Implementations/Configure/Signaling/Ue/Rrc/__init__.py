from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrcCls:
	"""Rrc commands group definition. 5 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrc", core, parent)

	@property
	def asn(self):
		"""asn commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_asn'):
			from .Asn import AsnCls
			self._asn = AsnCls(self._core, self._cmd_group)
		return self._asn

	def clone(self) -> 'RrcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RrcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
