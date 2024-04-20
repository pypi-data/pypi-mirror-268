from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def bwp(self):
		"""bwp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwp'):
			from .Bwp import BwpCls
			self._bwp = BwpCls(self._core, self._cmd_group)
		return self._bwp

	def get_value(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:NRADio:CELL \n
		Snippet: value: List[str] = driver.catalog.signaling.nradio.cell.get_value() \n
		Queries a list of all LTE or NR cells. \n
			:return: cell_name: Comma-separated list of cell names, one string per cell.
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:NRADio:CELL?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
