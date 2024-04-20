from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CnPagingCls:
	"""CnPaging commands group definition. 3 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnPaging", core, parent)

	@property
	def edRx(self):
		"""edRx commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_edRx'):
			from .EdRx import EdRxCls
			self._edRx = EdRxCls(self._core, self._cmd_group)
		return self._edRx

	def clone(self) -> 'CnPagingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CnPagingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
