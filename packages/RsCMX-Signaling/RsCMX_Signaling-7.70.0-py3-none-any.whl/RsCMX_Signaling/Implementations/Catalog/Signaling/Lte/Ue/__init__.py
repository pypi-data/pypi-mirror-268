from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCls:
	"""Ue commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ue", core, parent)

	@property
	def bearer(self):
		"""bearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bearer'):
			from .Bearer import BearerCls
			self._bearer = BearerCls(self._core, self._cmd_group)
		return self._bearer

	@property
	def dbearer(self):
		"""dbearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbearer'):
			from .Dbearer import DbearerCls
			self._dbearer = DbearerCls(self._core, self._cmd_group)
		return self._dbearer

	def clone(self) -> 'UeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
