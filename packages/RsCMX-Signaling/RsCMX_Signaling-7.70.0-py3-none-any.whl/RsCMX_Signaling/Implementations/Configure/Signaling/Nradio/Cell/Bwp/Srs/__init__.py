from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrsCls:
	"""Srs commands group definition. 19 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def cnCodebook(self):
		"""cnCodebook commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cnCodebook'):
			from .CnCodebook import CnCodebookCls
			self._cnCodebook = CnCodebookCls(self._core, self._cmd_group)
		return self._cnCodebook

	@property
	def aswitching(self):
		"""aswitching commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_aswitching'):
			from .Aswitching import AswitchingCls
			self._aswitching = AswitchingCls(self._core, self._cmd_group)
		return self._aswitching

	def clone(self) -> 'SrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
