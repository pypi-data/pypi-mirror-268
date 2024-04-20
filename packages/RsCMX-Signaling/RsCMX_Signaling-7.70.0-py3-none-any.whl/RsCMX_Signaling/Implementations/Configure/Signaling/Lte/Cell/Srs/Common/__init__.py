from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CommonCls:
	"""Common commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("common", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def sframe(self):
		"""sframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sframe'):
			from .Sframe import SframeCls
			self._sframe = SframeCls(self._core, self._cmd_group)
		return self._sframe

	@property
	def sant(self):
		"""sant commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sant'):
			from .Sant import SantCls
			self._sant = SantCls(self._core, self._cmd_group)
		return self._sant

	def clone(self) -> 'CommonCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CommonCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
