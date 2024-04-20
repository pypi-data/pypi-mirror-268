from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCapabilityCls:
	"""UeCapability commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueCapability", core, parent)

	@property
	def nradio(self):
		"""nradio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	@property
	def eutra(self):
		"""eutra commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eutra'):
			from .Eutra import EutraCls
			self._eutra = EutraCls(self._core, self._cmd_group)
		return self._eutra

	@property
	def mrdc(self):
		"""mrdc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mrdc'):
			from .Mrdc import MrdcCls
			self._mrdc = MrdcCls(self._core, self._cmd_group)
		return self._mrdc

	def clone(self) -> 'UeCapabilityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCapabilityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
