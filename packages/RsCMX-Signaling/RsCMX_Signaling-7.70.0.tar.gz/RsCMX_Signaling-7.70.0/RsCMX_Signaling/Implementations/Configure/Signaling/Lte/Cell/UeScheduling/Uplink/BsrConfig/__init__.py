from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BsrConfigCls:
	"""BsrConfig commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsrConfig", core, parent)

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Rb import RbCls
			self._rb = RbCls(self._core, self._cmd_group)
		return self._rb

	@property
	def mcsModes(self):
		"""mcsModes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsModes'):
			from .McsModes import McsModesCls
			self._mcsModes = McsModesCls(self._core, self._cmd_group)
		return self._mcsModes

	@property
	def morder(self):
		"""morder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_morder'):
			from .Morder import MorderCls
			self._morder = MorderCls(self._core, self._cmd_group)
		return self._morder

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	def clone(self) -> 'BsrConfigCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BsrConfigCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
