from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CwordCls:
	"""Cword commands group definition. 3 total commands, 3 Subgroups, 0 group commands
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
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_throughput'):
			from .Throughput import ThroughputCls
			self._throughput = ThroughputCls(self._core, self._cmd_group)
		return self._throughput

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	def clone(self) -> 'CwordCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CwordCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
