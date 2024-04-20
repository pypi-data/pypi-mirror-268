from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmeasureCls:
	"""Cmeasure commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmeasure", core, parent)

	@property
	def cgroup(self):
		"""cgroup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cgroup'):
			from .Cgroup import CgroupCls
			self._cgroup = CgroupCls(self._core, self._cmd_group)
		return self._cgroup

	def get_cells(self) -> List[str]:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:CMEasure:CELLs \n
		Snippet: value: List[str] = driver.configure.signaling.measurement.bler.cmeasure.get_cells() \n
		Selects the cells to be evaluated by the BLER measurement. \n
			:return: cell_name: Comma-separated list of cells
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:BLER:CMEasure:CELLs?')
		return Conversions.str_to_str_list(response)

	def set_cells(self, cell_name: List[str]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:CMEasure:CELLs \n
		Snippet: driver.configure.signaling.measurement.bler.cmeasure.set_cells(cell_name = ['abc1', 'abc2', 'abc3']) \n
		Selects the cells to be evaluated by the BLER measurement. \n
			:param cell_name: Comma-separated list of cells
		"""
		param = Conversions.list_to_csv_quoted_str(cell_name)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:CMEasure:CELLs {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.CellsTypeToMeasure:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:CMEasure \n
		Snippet: value: enums.CellsTypeToMeasure = driver.configure.signaling.measurement.bler.cmeasure.get_value() \n
		Selects the scope of the BLER measurement. \n
			:return: cells_to_measure: CGRoup: Measure certain cell groups, selected via [CONFigure:]SIGNaling:MEASurement:BLER:CMEasure:CGRoup. CELLs: Measure certain cells, selected via [CONFigure:]SIGNaling:MEASurement:BLER:CMEasure:CELLs.
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:BLER:CMEasure?')
		return Conversions.str_to_scalar_enum(response, enums.CellsTypeToMeasure)

	def set_value(self, cells_to_measure: enums.CellsTypeToMeasure) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:CMEasure \n
		Snippet: driver.configure.signaling.measurement.bler.cmeasure.set_value(cells_to_measure = enums.CellsTypeToMeasure.CELLs) \n
		Selects the scope of the BLER measurement. \n
			:param cells_to_measure: CGRoup: Measure certain cell groups, selected via [CONFigure:]SIGNaling:MEASurement:BLER:CMEasure:CGRoup. CELLs: Measure certain cells, selected via [CONFigure:]SIGNaling:MEASurement:BLER:CMEasure:CELLs.
		"""
		param = Conversions.enum_scalar_to_str(cells_to_measure, enums.CellsTypeToMeasure)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:CMEasure {param}')

	def clone(self) -> 'CmeasureCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CmeasureCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
