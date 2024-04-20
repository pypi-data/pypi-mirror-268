from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MconfigCls:
	"""Mconfig commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

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
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def csirsPorts(self):
		"""csirsPorts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csirsPorts'):
			from .CsirsPorts import CsirsPortsCls
			self._csirsPorts = CsirsPortsCls(self._core, self._cmd_group)
		return self._csirsPorts

	@property
	def aports(self):
		"""aports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aports'):
			from .Aports import AportsCls
			self._aports = AportsCls(self._core, self._cmd_group)
		return self._aports

	@property
	def cdeployment(self):
		"""cdeployment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdeployment'):
			from .Cdeployment import CdeploymentCls
			self._cdeployment = CdeploymentCls(self._core, self._cmd_group)
		return self._cdeployment

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import SspacingCls
			self._sspacing = SspacingCls(self._core, self._cmd_group)
		return self._sspacing

	@property
	def aoa(self):
		"""aoa commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoa'):
			from .Aoa import AoaCls
			self._aoa = AoaCls(self._core, self._cmd_group)
		return self._aoa

	def clone(self) -> 'MconfigCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MconfigCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
