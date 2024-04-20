from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RetransmCls:
	"""Retransm commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("retransm", core, parent)

	@property
	def rversion(self):
		"""rversion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rversion'):
			from .Rversion import RversionCls
			self._rversion = RversionCls(self._core, self._cmd_group)
		return self._rversion

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def ariv(self):
		"""ariv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ariv'):
			from .Ariv import ArivCls
			self._ariv = ArivCls(self._core, self._cmd_group)
		return self._ariv

	@property
	def rb(self):
		"""rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rb'):
			from .Rb import RbCls
			self._rb = RbCls(self._core, self._cmd_group)
		return self._rb

	@property
	def moffset(self):
		"""moffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_moffset'):
			from .Moffset import MoffsetCls
			self._moffset = MoffsetCls(self._core, self._cmd_group)
		return self._moffset

	def clone(self) -> 'RetransmCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RetransmCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
