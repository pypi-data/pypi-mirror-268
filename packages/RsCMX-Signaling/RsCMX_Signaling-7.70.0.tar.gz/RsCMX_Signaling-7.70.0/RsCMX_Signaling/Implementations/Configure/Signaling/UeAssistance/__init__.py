from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeAssistanceCls:
	"""UeAssistance commands group definition. 9 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueAssistance", core, parent)

	@property
	def nradio(self):
		"""nradio commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	def clone(self) -> 'UeAssistanceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeAssistanceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
