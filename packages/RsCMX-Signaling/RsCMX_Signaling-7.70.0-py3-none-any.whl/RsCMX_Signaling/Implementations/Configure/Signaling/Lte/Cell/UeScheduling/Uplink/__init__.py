from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 11 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def smode(self):
		"""smode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smode'):
			from .Smode import SmodeCls
			self._smode = SmodeCls(self._core, self._cmd_group)
		return self._smode

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def ttiBundling(self):
		"""ttiBundling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiBundling'):
			from .TtiBundling import TtiBundlingCls
			self._ttiBundling = TtiBundlingCls(self._core, self._cmd_group)
		return self._ttiBundling

	@property
	def igConfig(self):
		"""igConfig commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_igConfig'):
			from .IgConfig import IgConfigCls
			self._igConfig = IgConfigCls(self._core, self._cmd_group)
		return self._igConfig

	@property
	def bsrConfig(self):
		"""bsrConfig commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bsrConfig'):
			from .BsrConfig import BsrConfigCls
			self._bsrConfig = BsrConfigCls(self._core, self._cmd_group)
		return self._bsrConfig

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
