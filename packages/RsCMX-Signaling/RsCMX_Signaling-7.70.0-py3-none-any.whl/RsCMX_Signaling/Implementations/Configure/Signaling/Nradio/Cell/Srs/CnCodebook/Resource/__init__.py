from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResourceCls:
	"""Resource commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resource", core, parent)

	@property
	def resource(self):
		"""resource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resource'):
			from .Resource import ResourceCls
			self._resource = ResourceCls(self._core, self._cmd_group)
		return self._resource

	@property
	def tcomb(self):
		"""tcomb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcomb'):
			from .Tcomb import TcombCls
			self._tcomb = TcombCls(self._core, self._cmd_group)
		return self._tcomb

	@property
	def rmapping(self):
		"""rmapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmapping'):
			from .Rmapping import RmappingCls
			self._rmapping = RmappingCls(self._core, self._cmd_group)
		return self._rmapping

	@property
	def fhopping(self):
		"""fhopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhopping'):
			from .Fhopping import FhoppingCls
			self._fhopping = FhoppingCls(self._core, self._cmd_group)
		return self._fhopping

	@property
	def rtype(self):
		"""rtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtype'):
			from .Rtype import RtypeCls
			self._rtype = RtypeCls(self._core, self._cmd_group)
		return self._rtype

	def clone(self) -> 'ResourceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResourceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
