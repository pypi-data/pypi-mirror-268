from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FadingCls:
	"""Fading commands group definition. 7 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fading", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profile'):
			from .Profile import ProfileCls
			self._profile = ProfileCls(self._core, self._cmd_group)
		return self._profile

	@property
	def seed(self):
		"""seed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seed'):
			from .Seed import SeedCls
			self._seed = SeedCls(self._core, self._cmd_group)
		return self._seed

	@property
	def iloss(self):
		"""iloss commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_iloss'):
			from .Iloss import IlossCls
			self._iloss = IlossCls(self._core, self._cmd_group)
		return self._iloss

	@property
	def dshift(self):
		"""dshift commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dshift'):
			from .Dshift import DshiftCls
			self._dshift = DshiftCls(self._core, self._cmd_group)
		return self._dshift

	def clone(self) -> 'FadingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FadingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
