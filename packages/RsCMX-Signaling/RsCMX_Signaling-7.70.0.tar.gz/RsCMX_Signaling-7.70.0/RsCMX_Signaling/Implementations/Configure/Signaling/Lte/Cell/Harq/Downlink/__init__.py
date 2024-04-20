from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 7 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def reTx(self):
		"""reTx commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_reTx'):
			from .ReTx import ReTxCls
			self._reTx = ReTxCls(self._core, self._cmd_group)
		return self._reTx

	@property
	def psOrder(self):
		"""psOrder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psOrder'):
			from .PsOrder import PsOrderCls
			self._psOrder = PsOrderCls(self._core, self._cmd_group)
		return self._psOrder

	@property
	def rvSequence(self):
		"""rvSequence commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvSequence'):
			from .RvSequence import RvSequenceCls
			self._rvSequence = RvSequenceCls(self._core, self._cmd_group)
		return self._rvSequence

	@property
	def mcsBehavior(self):
		"""mcsBehavior commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsBehavior'):
			from .McsBehavior import McsBehaviorCls
			self._mcsBehavior = McsBehaviorCls(self._core, self._cmd_group)
		return self._mcsBehavior

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
