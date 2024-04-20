from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCls:
	"""Lte commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	@property
	def cell(self):
		"""cell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	@property
	def vcell(self):
		"""vcell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vcell'):
			from .Vcell import VcellCls
			self._vcell = VcellCls(self._core, self._cmd_group)
		return self._vcell

	def set_cgroup(self, cell_group_name: str) -> None:
		"""SCPI: CREate:SIGNaling:LTE:CGRoup \n
		Snippet: driver.create.signaling.lte.set_cgroup(cell_group_name = 'abc') \n
		Creates an LTE or NR cell group. Assign a unique name to each named object within the test environment. Assigning an
		already used name can be rejected with an error message, even if the other object has not the same type as the new object. \n
			:param cell_group_name: Assigns a name to the cell group. The string is used in other commands to select this cell group.
		"""
		param = Conversions.value_to_quoted_str(cell_group_name)
		self._core.io.write(f'CREate:SIGNaling:LTE:CGRoup {param}')

	def clone(self) -> 'LteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
