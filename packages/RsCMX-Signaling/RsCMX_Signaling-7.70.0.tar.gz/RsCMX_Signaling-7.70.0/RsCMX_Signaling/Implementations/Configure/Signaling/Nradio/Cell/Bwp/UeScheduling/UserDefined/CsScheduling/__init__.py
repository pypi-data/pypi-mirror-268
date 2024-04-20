from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsSchedulingCls:
	"""CsScheduling commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csScheduling", core, parent)

	@property
	def k0(self):
		"""k0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k0'):
			from .K0 import K0Cls
			self._k0 = K0Cls(self._core, self._cmd_group)
		return self._k0

	@property
	def k2(self):
		"""k2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_k2'):
			from .K2 import K2Cls
			self._k2 = K2Cls(self._core, self._cmd_group)
		return self._k2

	def clone(self) -> 'CsSchedulingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CsSchedulingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
