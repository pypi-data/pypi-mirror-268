from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsbCls:
	"""Ssb commands group definition. 11 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssb", core, parent)

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Soffset import SoffsetCls
			self._soffset = SoffsetCls(self._core, self._cmd_group)
		return self._soffset

	@property
	def paOffset(self):
		"""paOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paOffset'):
			from .PaOffset import PaOffsetCls
			self._paOffset = PaOffsetCls(self._core, self._cmd_group)
		return self._paOffset

	@property
	def afrequency(self):
		"""afrequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_afrequency'):
			from .Afrequency import AfrequencyCls
			self._afrequency = AfrequencyCls(self._core, self._cmd_group)
		return self._afrequency

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	@property
	def periodicity(self):
		"""periodicity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_periodicity'):
			from .Periodicity import PeriodicityCls
			self._periodicity = PeriodicityCls(self._core, self._cmd_group)
		return self._periodicity

	@property
	def hfOffset(self):
		"""hfOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hfOffset'):
			from .HfOffset import HfOffsetCls
			self._hfOffset = HfOffsetCls(self._core, self._cmd_group)
		return self._hfOffset

	@property
	def transmission(self):
		"""transmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transmission'):
			from .Transmission import TransmissionCls
			self._transmission = TransmissionCls(self._core, self._cmd_group)
		return self._transmission

	@property
	def beam(self):
		"""beam commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_beam'):
			from .Beam import BeamCls
			self._beam = BeamCls(self._core, self._cmd_group)
		return self._beam

	def clone(self) -> 'SsbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SsbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
