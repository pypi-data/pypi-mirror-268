from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCls:
	"""Lte commands group definition. 6 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

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
	def ue(self):
		"""ue commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	def get_cell(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:LTE:CELL \n
		Snippet: value: List[str] = driver.catalog.signaling.lte.get_cell() \n
		Queries a list of all LTE or NR cells. \n
			:return: cell_name: Comma-separated list of cell names, one string per cell.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:LTE:CELL?')
		return Conversions.str_to_str_list(response)

	def get_cgroup(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:LTE:CGRoup \n
		Snippet: value: List[str] = driver.catalog.signaling.lte.get_cgroup() \n
		Queries a list of all LTE or NR cell groups. \n
			:return: cell_group_name: Comma-separated list of cell group names, one string per cell group.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:LTE:CGRoup?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'LteCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LteCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
