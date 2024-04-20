from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SecondaryCls:
	"""Secondary commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("secondary", core, parent)

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
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def cgroup(self):
		"""cgroup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cgroup'):
			from .Cgroup import CgroupCls
			self._cgroup = CgroupCls(self._core, self._cmd_group)
		return self._cgroup

	@property
	def woLanguage(self):
		"""woLanguage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_woLanguage'):
			from .WoLanguage import WoLanguageCls
			self._woLanguage = WoLanguageCls(self._core, self._cmd_group)
		return self._woLanguage

	@property
	def language(self):
		"""language commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_language'):
			from .Language import LanguageCls
			self._language = LanguageCls(self._core, self._cmd_group)
		return self._language

	@property
	def serial(self):
		"""serial commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_serial'):
			from .Serial import SerialCls
			self._serial = SerialCls(self._core, self._cmd_group)
		return self._serial

	def clone(self) -> 'SecondaryCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SecondaryCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
