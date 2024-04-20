from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcrntiCls:
	"""Ccrnti commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccrnti", core, parent)

	@property
	def send(self):
		"""send commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_send'):
			from .Send import SendCls
			self._send = SendCls(self._core, self._cmd_group)
		return self._send

	@property
	def pdcchFormat(self):
		"""pdcchFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdcchFormat'):
			from .PdcchFormat import PdcchFormatCls
			self._pdcchFormat = PdcchFormatCls(self._core, self._cmd_group)
		return self._pdcchFormat

	def clone(self) -> 'CcrntiCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcrntiCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
