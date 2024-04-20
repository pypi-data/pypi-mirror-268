from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 19 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def routing(self):
		"""routing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_routing'):
			from .Routing import RoutingCls
			self._routing = RoutingCls(self._core, self._cmd_group)
		return self._routing

	@property
	def logging(self):
		"""logging commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_logging'):
			from .Logging import LoggingCls
			self._logging = LoggingCls(self._core, self._cmd_group)
		return self._logging

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
	def topology(self):
		"""topology commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Topology import TopologyCls
			self._topology = TopologyCls(self._core, self._cmd_group)
		return self._topology

	@property
	def register(self):
		"""register commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_register'):
			from .Register import RegisterCls
			self._register = RegisterCls(self._core, self._cmd_group)
		return self._register

	@property
	def registration(self):
		"""registration commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_registration'):
			from .Registration import RegistrationCls
			self._registration = RegistrationCls(self._core, self._cmd_group)
		return self._registration

	@property
	def dapi(self):
		"""dapi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dapi'):
			from .Dapi import DapiCls
			self._dapi = DapiCls(self._core, self._cmd_group)
		return self._dapi

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
