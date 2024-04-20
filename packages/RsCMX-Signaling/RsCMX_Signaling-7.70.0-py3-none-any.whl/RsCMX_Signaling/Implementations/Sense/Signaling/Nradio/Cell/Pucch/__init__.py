from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PucchCls:
	"""Pucch commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def nsymbols(self):
		"""nsymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsymbols'):
			from .Nsymbols import NsymbolsCls
			self._nsymbols = NsymbolsCls(self._core, self._cmd_group)
		return self._nsymbols

	@property
	def ssIndex(self):
		"""ssIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssIndex'):
			from .SsIndex import SsIndexCls
			self._ssIndex = SsIndexCls(self._core, self._cmd_group)
		return self._ssIndex

	def clone(self) -> 'PucchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PucchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
