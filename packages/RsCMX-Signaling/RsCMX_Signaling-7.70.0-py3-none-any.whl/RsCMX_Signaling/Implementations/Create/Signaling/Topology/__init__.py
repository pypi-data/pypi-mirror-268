from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TopologyCls:
	"""Topology commands group definition. 6 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("topology", core, parent)

	@property
	def cnetwork(self):
		"""cnetwork commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cnetwork'):
			from .Cnetwork import CnetworkCls
			self._cnetwork = CnetworkCls(self._core, self._cmd_group)
		return self._cnetwork

	@property
	def plmn(self):
		"""plmn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plmn'):
			from .Plmn import PlmnCls
			self._plmn = PlmnCls(self._core, self._cmd_group)
		return self._plmn

	@property
	def eps(self):
		"""eps commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eps'):
			from .Eps import EpsCls
			self._eps = EpsCls(self._core, self._cmd_group)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fgs'):
			from .Fgs import FgsCls
			self._fgs = FgsCls(self._core, self._cmd_group)
		return self._fgs

	def clone(self) -> 'TopologyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TopologyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
