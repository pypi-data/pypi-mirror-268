from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CwordCls:
	"""Cword commands group definition. 4 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: Cword, default value after init: Cword.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cword", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cword_get', 'repcap_cword_set', repcap.Cword.Nr1)

	def repcap_cword_set(self, cword: repcap.Cword) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Cword.Default
		Default value after init: Cword.Nr1"""
		self._cmd_group.set_repcap_enum_value(cword)

	def repcap_cword_get(self) -> repcap.Cword:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def tbsIndex(self):
		"""tbsIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsIndex'):
			from .TbsIndex import TbsIndexCls
			self._tbsIndex = TbsIndexCls(self._core, self._cmd_group)
		return self._tbsIndex

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import McsCls
			self._mcs = McsCls(self._core, self._cmd_group)
		return self._mcs

	@property
	def tbsBits(self):
		"""tbsBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbsBits'):
			from .TbsBits import TbsBitsCls
			self._tbsBits = TbsBitsCls(self._core, self._cmd_group)
		return self._tbsBits

	@property
	def crtype(self):
		"""crtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crtype'):
			from .Crtype import CrtypeCls
			self._crtype = CrtypeCls(self._core, self._cmd_group)
		return self._crtype

	def clone(self) -> 'CwordCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CwordCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
