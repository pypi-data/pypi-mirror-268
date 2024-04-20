from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 20 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	@property
	def mobility(self):
		"""mobility commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mobility'):
			from .Mobility import MobilityCls
			self._mobility = MobilityCls(self._core, self._cmd_group)
		return self._mobility

	@property
	def nrdc(self):
		"""nrdc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_nrdc'):
			from .Nrdc import NrdcCls
			self._nrdc = NrdcCls(self._core, self._cmd_group)
		return self._nrdc

	@property
	def nradio(self):
		"""nradio commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	@property
	def sms(self):
		"""sms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sms'):
			from .Sms import SmsCls
			self._sms = SmsCls(self._core, self._cmd_group)
		return self._sms

	@property
	def apMod(self):
		"""apMod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apMod'):
			from .ApMod import ApModCls
			self._apMod = ApModCls(self._core, self._cmd_group)
		return self._apMod

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
