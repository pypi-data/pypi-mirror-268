from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def earfcn(self):
		"""earfcn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_earfcn'):
			from .Earfcn import EarfcnCls
			self._earfcn = EarfcnCls(self._core, self._cmd_group)
		return self._earfcn

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def rblocks(self):
		"""rblocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rblocks'):
			from .Rblocks import RblocksCls
			self._rblocks = RblocksCls(self._core, self._cmd_group)
		return self._rblocks

	@property
	def rchoice(self):
		"""rchoice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rchoice'):
			from .Rchoice import RchoiceCls
			self._rchoice = RchoiceCls(self._core, self._cmd_group)
		return self._rchoice

	@property
	def freqError(self):
		"""freqError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
