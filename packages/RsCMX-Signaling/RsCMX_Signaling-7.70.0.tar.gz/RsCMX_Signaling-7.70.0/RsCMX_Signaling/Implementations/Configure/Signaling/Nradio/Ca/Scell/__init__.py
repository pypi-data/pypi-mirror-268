from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScellCls:
	"""Scell commands group definition. 7 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scell", core, parent)

	@property
	def activation(self):
		"""activation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_activation'):
			from .Activation import ActivationCls
			self._activation = ActivationCls(self._core, self._cmd_group)
		return self._activation

	@property
	def mac(self):
		"""mac commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import MacCls
			self._mac = MacCls(self._core, self._cmd_group)
		return self._mac

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	@property
	def dormancy(self):
		"""dormancy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dormancy'):
			from .Dormancy import DormancyCls
			self._dormancy = DormancyCls(self._core, self._cmd_group)
		return self._dormancy

	def clone(self) -> 'ScellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
