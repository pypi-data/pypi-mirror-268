from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmMappingCls:
	"""CmMapping commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmMapping", core, parent)

	@property
	def nsubframe(self):
		"""nsubframe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nsubframe'):
			from .Nsubframe import NsubframeCls
			self._nsubframe = NsubframeCls(self._core, self._cmd_group)
		return self._nsubframe

	@property
	def csirs(self):
		"""csirs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import CsirsCls
			self._csirs = CsirsCls(self._core, self._cmd_group)
		return self._csirs

	@property
	def ssubframe(self):
		"""ssubframe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ssubframe'):
			from .Ssubframe import SsubframeCls
			self._ssubframe = SsubframeCls(self._core, self._cmd_group)
		return self._ssubframe

	def clone(self) -> 'CmMappingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CmMappingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
