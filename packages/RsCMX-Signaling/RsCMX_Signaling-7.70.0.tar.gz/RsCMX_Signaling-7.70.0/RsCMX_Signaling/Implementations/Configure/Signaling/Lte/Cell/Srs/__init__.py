from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrsCls:
	"""Srs commands group definition. 8 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def common(self):
		"""common commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_common'):
			from .Common import CommonCls
			self._common = CommonCls(self._core, self._cmd_group)
		return self._common

	@property
	def dedicated(self):
		"""dedicated commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dedicated'):
			from .Dedicated import DedicatedCls
			self._dedicated = DedicatedCls(self._core, self._cmd_group)
		return self._dedicated

	def clone(self) -> 'SrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
