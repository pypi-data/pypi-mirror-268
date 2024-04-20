from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def apoint(self):
		"""apoint commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apoint'):
			from .Apoint import ApointCls
			self._apoint = ApointCls(self._core, self._cmd_group)
		return self._apoint

	@property
	def cfrequency(self):
		"""cfrequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfrequency'):
			from .Cfrequency import CfrequencyCls
			self._cfrequency = CfrequencyCls(self._core, self._cmd_group)
		return self._cfrequency

	@property
	def ibwp(self):
		"""ibwp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ibwp'):
			from .Ibwp import IbwpCls
			self._ibwp = IbwpCls(self._core, self._cmd_group)
		return self._ibwp

	@property
	def ocarrier(self):
		"""ocarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocarrier'):
			from .Ocarrier import OcarrierCls
			self._ocarrier = OcarrierCls(self._core, self._cmd_group)
		return self._ocarrier

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
