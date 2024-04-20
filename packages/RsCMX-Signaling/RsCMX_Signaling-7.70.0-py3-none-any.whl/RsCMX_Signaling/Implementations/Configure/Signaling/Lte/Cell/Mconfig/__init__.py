from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MconfigCls:
	"""Mconfig commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mconfig", core, parent)

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def crSports(self):
		"""crSports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crSports'):
			from .CrSports import CrSportsCls
			self._crSports = CrSportsCls(self._core, self._cmd_group)
		return self._crSports

	@property
	def csirsPorts(self):
		"""csirsPorts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csirsPorts'):
			from .CsirsPorts import CsirsPortsCls
			self._csirsPorts = CsirsPortsCls(self._core, self._cmd_group)
		return self._csirsPorts

	@property
	def cdeployment(self):
		"""cdeployment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdeployment'):
			from .Cdeployment import CdeploymentCls
			self._cdeployment = CdeploymentCls(self._core, self._cmd_group)
		return self._cdeployment

	@property
	def dlOnly(self):
		"""dlOnly commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlOnly'):
			from .DlOnly import DlOnlyCls
			self._dlOnly = DlOnlyCls(self._core, self._cmd_group)
		return self._dlOnly

	def clone(self) -> 'MconfigCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MconfigCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
