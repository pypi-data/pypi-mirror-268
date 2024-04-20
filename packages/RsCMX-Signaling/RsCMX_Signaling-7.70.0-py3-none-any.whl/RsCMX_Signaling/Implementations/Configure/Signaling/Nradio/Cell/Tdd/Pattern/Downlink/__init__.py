from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def nslots(self):
		"""nslots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nslots'):
			from .Nslots import NslotsCls
			self._nslots = NslotsCls(self._core, self._cmd_group)
		return self._nslots

	@property
	def fsSymbol(self):
		"""fsSymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsSymbol'):
			from .FsSymbol import FsSymbolCls
			self._fsSymbol = FsSymbolCls(self._core, self._cmd_group)
		return self._fsSymbol

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
