from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	@property
	def timer(self):
		"""timer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_timer'):
			from .Timer import TimerCls
			self._timer = TimerCls(self._core, self._cmd_group)
		return self._timer

	@property
	def taCode(self):
		"""taCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taCode'):
			from .TaCode import TaCodeCls
			self._taCode = TaCodeCls(self._core, self._cmd_group)
		return self._taCode

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import InfoCls
			self._info = InfoCls(self._core, self._cmd_group)
		return self._info

	def clone(self) -> 'EpsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EpsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
