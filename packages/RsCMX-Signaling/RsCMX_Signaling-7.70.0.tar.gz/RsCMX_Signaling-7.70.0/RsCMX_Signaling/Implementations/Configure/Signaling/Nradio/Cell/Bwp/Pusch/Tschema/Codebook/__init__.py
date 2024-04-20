from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CodebookCls:
	"""Codebook commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("codebook", core, parent)

	@property
	def subset(self):
		"""subset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subset'):
			from .Subset import SubsetCls
			self._subset = SubsetCls(self._core, self._cmd_group)
		return self._subset

	@property
	def fptMode(self):
		"""fptMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fptMode'):
			from .FptMode import FptModeCls
			self._fptMode = FptModeCls(self._core, self._cmd_group)
		return self._fptMode

	def clone(self) -> 'CodebookCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CodebookCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
