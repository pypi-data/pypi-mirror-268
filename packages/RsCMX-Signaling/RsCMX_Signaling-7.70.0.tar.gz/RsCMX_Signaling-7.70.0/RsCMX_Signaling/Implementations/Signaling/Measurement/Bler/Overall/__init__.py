from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OverallCls:
	"""Overall commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("overall", core, parent)

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_throughput'):
			from .Throughput import ThroughputCls
			self._throughput = ThroughputCls(self._core, self._cmd_group)
		return self._throughput

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	@property
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_confidence'):
			from .Confidence import ConfidenceCls
			self._confidence = ConfidenceCls(self._core, self._cmd_group)
		return self._confidence

	def clone(self) -> 'OverallCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OverallCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
