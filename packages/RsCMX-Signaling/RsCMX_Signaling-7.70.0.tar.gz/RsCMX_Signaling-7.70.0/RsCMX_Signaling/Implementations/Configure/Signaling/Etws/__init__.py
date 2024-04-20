from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EtwsCls:
	"""Etws commands group definition. 12 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("etws", core, parent)

	@property
	def tranmission(self):
		"""tranmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tranmission'):
			from .Tranmission import TranmissionCls
			self._tranmission = TranmissionCls(self._core, self._cmd_group)
		return self._tranmission

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import IdCls
			self._id = IdCls(self._core, self._cmd_group)
		return self._id

	@property
	def serial(self):
		"""serial commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_serial'):
			from .Serial import SerialCls
			self._serial = SerialCls(self._core, self._cmd_group)
		return self._serial

	@property
	def alert(self):
		"""alert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alert'):
			from .Alert import AlertCls
			self._alert = AlertCls(self._core, self._cmd_group)
		return self._alert

	@property
	def popup(self):
		"""popup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_popup'):
			from .Popup import PopupCls
			self._popup = PopupCls(self._core, self._cmd_group)
		return self._popup

	@property
	def secondary(self):
		"""secondary commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_secondary'):
			from .Secondary import SecondaryCls
			self._secondary = SecondaryCls(self._core, self._cmd_group)
		return self._secondary

	def clone(self) -> 'EtwsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EtwsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
