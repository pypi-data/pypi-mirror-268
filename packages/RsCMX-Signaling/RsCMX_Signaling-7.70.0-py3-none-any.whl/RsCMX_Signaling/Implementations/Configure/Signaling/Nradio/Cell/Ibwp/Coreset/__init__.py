from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CoresetCls:
	"""Coreset commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coreset", core, parent)

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import DurationCls
			self._duration = DurationCls(self._core, self._cmd_group)
		return self._duration

	@property
	def fdrBitmap(self):
		"""fdrBitmap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdrBitmap'):
			from .FdrBitmap import FdrBitmapCls
			self._fdrBitmap = FdrBitmapCls(self._core, self._cmd_group)
		return self._fdrBitmap

	@property
	def rmatching(self):
		"""rmatching commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmatching'):
			from .Rmatching import RmatchingCls
			self._rmatching = RmatchingCls(self._core, self._cmd_group)
		return self._rmatching

	@property
	def ncandidates(self):
		"""ncandidates commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncandidates'):
			from .Ncandidates import NcandidatesCls
			self._ncandidates = NcandidatesCls(self._core, self._cmd_group)
		return self._ncandidates

	def clone(self) -> 'CoresetCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CoresetCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
