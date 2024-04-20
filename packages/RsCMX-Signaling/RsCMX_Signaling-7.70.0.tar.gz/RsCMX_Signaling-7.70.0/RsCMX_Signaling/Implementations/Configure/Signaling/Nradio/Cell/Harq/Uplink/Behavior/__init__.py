from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BehaviorCls:
	"""Behavior commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("behavior", core, parent)

	@property
	def crcPass(self):
		"""crcPass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crcPass'):
			from .CrcPass import CrcPassCls
			self._crcPass = CrcPassCls(self._core, self._cmd_group)
		return self._crcPass

	@property
	def nulPower(self):
		"""nulPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nulPower'):
			from .NulPower import NulPowerCls
			self._nulPower = NulPowerCls(self._core, self._cmd_group)
		return self._nulPower

	def clone(self) -> 'BehaviorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BehaviorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
