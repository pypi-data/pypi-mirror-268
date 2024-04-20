from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ControlCls:
	"""Control commands group definition. 16 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	@property
	def spbPower(self):
		"""spbPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spbPower'):
			from .SpbPower import SpbPowerCls
			self._spbPower = SpbPowerCls(self._core, self._cmd_group)
		return self._spbPower

	@property
	def pnwGrant(self):
		"""pnwGrant commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnwGrant'):
			from .PnwGrant import PnwGrantCls
			self._pnwGrant = PnwGrantCls(self._core, self._cmd_group)
		return self._pnwGrant

	@property
	def pmax(self):
		"""pmax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmax'):
			from .Pmax import PmaxCls
			self._pmax = PmaxCls(self._core, self._cmd_group)
		return self._pmax

	@property
	def pnrFr1(self):
		"""pnrFr1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnrFr1'):
			from .PnrFr1 import PnrFr1Cls
			self._pnrFr1 = PnrFr1Cls(self._core, self._cmd_group)
		return self._pnrFr1

	@property
	def palphaSet(self):
		"""palphaSet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_palphaSet'):
			from .PalphaSet import PalphaSetCls
			self._palphaSet = PalphaSetCls(self._core, self._cmd_group)
		return self._palphaSet

	@property
	def tpControl(self):
		"""tpControl commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpControl'):
			from .TpControl import TpControlCls
			self._tpControl = TpControlCls(self._core, self._cmd_group)
		return self._tpControl

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def pbpiBpsk(self):
		"""pbpiBpsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbpiBpsk'):
			from .PbpiBpsk import PbpiBpskCls
			self._pbpiBpsk = PbpiBpskCls(self._core, self._cmd_group)
		return self._pbpiBpsk

	def clone(self) -> 'ControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
