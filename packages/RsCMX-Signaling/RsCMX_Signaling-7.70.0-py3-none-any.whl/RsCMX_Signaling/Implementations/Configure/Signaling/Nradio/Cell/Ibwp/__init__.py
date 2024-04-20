from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IbwpCls:
	"""Ibwp commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ibwp", core, parent)

	@property
	def coreset(self):
		"""coreset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_coreset'):
			from .Coreset import CoresetCls
			self._coreset = CoresetCls(self._core, self._cmd_group)
		return self._coreset

	@property
	def rcap(self):
		"""rcap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcap'):
			from .Rcap import RcapCls
			self._rcap = RcapCls(self._core, self._cmd_group)
		return self._rcap

	def clone(self) -> 'IbwpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IbwpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
