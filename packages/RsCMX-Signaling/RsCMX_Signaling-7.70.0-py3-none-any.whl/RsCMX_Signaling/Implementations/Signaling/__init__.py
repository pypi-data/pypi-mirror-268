from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 80 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def topology(self):
		"""topology commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Topology import TopologyCls
			self._topology = TopologyCls(self._core, self._cmd_group)
		return self._topology

	@property
	def log(self):
		"""log commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_log'):
			from .Log import LogCls
			self._log = LogCls(self._core, self._cmd_group)
		return self._log

	@property
	def ue(self):
		"""ue commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	@property
	def sms(self):
		"""sms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sms'):
			from .Sms import SmsCls
			self._sms = SmsCls(self._core, self._cmd_group)
		return self._sms

	@property
	def eps(self):
		"""eps commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eps'):
			from .Eps import EpsCls
			self._eps = EpsCls(self._core, self._cmd_group)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fgs'):
			from .Fgs import FgsCls
			self._fgs = FgsCls(self._core, self._cmd_group)
		return self._fgs

	@property
	def lte(self):
		"""lte commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def measurement(self):
		"""measurement commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def nradio(self):
		"""nradio commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	@property
	def rfChannel(self):
		"""rfChannel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfChannel'):
			from .RfChannel import RfChannelCls
			self._rfChannel = RfChannelCls(self._core, self._cmd_group)
		return self._rfChannel

	@property
	def fading(self):
		"""fading commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fading'):
			from .Fading import FadingCls
			self._fading = FadingCls(self._core, self._cmd_group)
		return self._fading

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
