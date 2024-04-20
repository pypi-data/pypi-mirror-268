from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResourceCls:
	"""Resource commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resource", core, parent)

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import OffsetCls
			self._offset = OffsetCls(self._core, self._cmd_group)
		return self._offset

	@property
	def ports(self):
		"""ports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import PortsCls
			self._ports = PortsCls(self._core, self._cmd_group)
		return self._ports

	@property
	def foSymbol(self):
		"""foSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_foSymbol'):
			from .FoSymbol import FoSymbolCls
			self._foSymbol = FoSymbolCls(self._core, self._cmd_group)
		return self._foSymbol

	@property
	def poVsss(self):
		"""poVsss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poVsss'):
			from .PoVsss import PoVsssCls
			self._poVsss = PoVsssCls(self._core, self._cmd_group)
		return self._poVsss

	def clone(self) -> 'ResourceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResourceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
