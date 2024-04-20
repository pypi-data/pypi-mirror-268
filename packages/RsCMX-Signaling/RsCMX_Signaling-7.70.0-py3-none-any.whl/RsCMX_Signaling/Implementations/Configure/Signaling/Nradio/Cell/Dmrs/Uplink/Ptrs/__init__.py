from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtrsCls:
	"""Ptrs commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptrs", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def tpEnable(self):
		"""tpEnable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpEnable'):
			from .TpEnable import TpEnableCls
			self._tpEnable = TpEnableCls(self._core, self._cmd_group)
		return self._tpEnable

	@property
	def tpDisable(self):
		"""tpDisable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpDisable'):
			from .TpDisable import TpDisableCls
			self._tpDisable = TpDisableCls(self._core, self._cmd_group)
		return self._tpDisable

	def clone(self) -> 'PtrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PtrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
