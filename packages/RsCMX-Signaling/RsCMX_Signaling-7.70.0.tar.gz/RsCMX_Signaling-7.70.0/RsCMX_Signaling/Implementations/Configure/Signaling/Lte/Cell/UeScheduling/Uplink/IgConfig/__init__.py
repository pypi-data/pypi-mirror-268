from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IgConfigCls:
	"""IgConfig commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("igConfig", core, parent)

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Rb import RbCls
			self._rb = RbCls(self._core, self._cmd_group)
		return self._rb

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def srcIndex(self):
		"""srcIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srcIndex'):
			from .SrcIndex import SrcIndexCls
			self._srcIndex = SrcIndexCls(self._core, self._cmd_group)
		return self._srcIndex

	@property
	def srprIndex(self):
		"""srprIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srprIndex'):
			from .SrprIndex import SrprIndexCls
			self._srprIndex = SrprIndexCls(self._core, self._cmd_group)
		return self._srprIndex

	def clone(self) -> 'IgConfigCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IgConfigCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
