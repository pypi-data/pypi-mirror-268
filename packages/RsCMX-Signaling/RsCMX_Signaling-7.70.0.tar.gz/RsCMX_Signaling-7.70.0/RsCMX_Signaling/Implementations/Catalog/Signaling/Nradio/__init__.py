from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NradioCls:
	"""Nradio commands group definition. 5 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nradio", core, parent)

	@property
	def ca(self):
		"""ca commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ca'):
			from .Ca import CaCls
			self._ca = CaCls(self._core, self._cmd_group)
		return self._ca

	@property
	def ncell(self):
		"""ncell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncell'):
			from .Ncell import NcellCls
			self._ncell = NcellCls(self._core, self._cmd_group)
		return self._ncell

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	def get_cgroup(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:NRADio:CGRoup \n
		Snippet: value: List[str] = driver.catalog.signaling.nradio.get_cgroup() \n
		Queries a list of all LTE or NR cell groups. \n
			:return: cell_group_name: Comma-separated list of cell group names, one string per cell group.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:NRADio:CGRoup?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'NradioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NradioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
