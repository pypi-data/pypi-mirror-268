from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NradioCls:
	"""Nradio commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nradio", core, parent)

	@property
	def cword(self):
		"""cword commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cword'):
			from .Cword import CwordCls
			self._cword = CwordCls(self._core, self._cmd_group)
		return self._cword

	@property
	def ri(self):
		"""ri commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ri'):
			from .Ri import RiCls
			self._ri = RiCls(self._core, self._cmd_group)
		return self._ri

	def clone(self) -> 'NradioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NradioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
