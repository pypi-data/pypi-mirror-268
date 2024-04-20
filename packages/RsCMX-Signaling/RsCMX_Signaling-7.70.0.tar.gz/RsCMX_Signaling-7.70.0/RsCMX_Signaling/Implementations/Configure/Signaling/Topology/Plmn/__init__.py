from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlmnCls:
	"""Plmn commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plmn", core, parent)

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import InfoCls
			self._info = InfoCls(self._core, self._cmd_group)
		return self._info

	@property
	def mnc(self):
		"""mnc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mnc'):
			from .Mnc import MncCls
			self._mnc = MncCls(self._core, self._cmd_group)
		return self._mnc

	@property
	def mcc(self):
		"""mcc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcc'):
			from .Mcc import MccCls
			self._mcc = MccCls(self._core, self._cmd_group)
		return self._mcc

	@property
	def epsFallback(self):
		"""epsFallback commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epsFallback'):
			from .EpsFallback import EpsFallbackCls
			self._epsFallback = EpsFallbackCls(self._core, self._cmd_group)
		return self._epsFallback

	@property
	def fgsFallback(self):
		"""fgsFallback commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fgsFallback'):
			from .FgsFallback import FgsFallbackCls
			self._fgsFallback = FgsFallbackCls(self._core, self._cmd_group)
		return self._fgsFallback

	@property
	def smeBearers(self):
		"""smeBearers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smeBearers'):
			from .SmeBearers import SmeBearersCls
			self._smeBearers = SmeBearersCls(self._core, self._cmd_group)
		return self._smeBearers

	def clone(self) -> 'PlmnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlmnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
