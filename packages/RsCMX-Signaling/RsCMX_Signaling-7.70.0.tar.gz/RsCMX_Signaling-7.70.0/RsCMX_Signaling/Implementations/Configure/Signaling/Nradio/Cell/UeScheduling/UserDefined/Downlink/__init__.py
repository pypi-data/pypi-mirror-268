from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def padding(self):
		"""padding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_padding'):
			from .Padding import PaddingCls
			self._padding = PaddingCls(self._core, self._cmd_group)
		return self._padding

	@property
	def bpid(self):
		"""bpid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bpid'):
			from .Bpid import BpidCls
			self._bpid = BpidCls(self._core, self._cmd_group)
		return self._bpid

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import AlevelCls
			self._alevel = AlevelCls(self._core, self._cmd_group)
		return self._alevel

	@property
	def ssid(self):
		"""ssid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssid'):
			from .Ssid import SsidCls
			self._ssid = SsidCls(self._core, self._cmd_group)
		return self._ssid

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def vpMapping(self):
		"""vpMapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vpMapping'):
			from .VpMapping import VpMappingCls
			self._vpMapping = VpMappingCls(self._core, self._cmd_group)
		return self._vpMapping

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
