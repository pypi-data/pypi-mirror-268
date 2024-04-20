from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.NeighborCellType:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
		Snippet: value: enums.NeighborCellType = driver.configure.signaling.measurement.ueReport.ncell.result.get_type_py() \n
		Selects the type of neighbor cell list to be used for neighbor cell measurements. \n
			:return: type_py: CNETwork: all created cells except the serving cell SIB: SIB neighbor cell list (configured neighbors of serving cell) NCList: for future use
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.NeighborCellType)

	def set_type_py(self, type_py: enums.NeighborCellType) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.result.set_type_py(type_py = enums.NeighborCellType.CNETwork) \n
		Selects the type of neighbor cell list to be used for neighbor cell measurements. \n
			:param type_py: CNETwork: all created cells except the serving cell SIB: SIB neighbor cell list (configured neighbors of serving cell) NCList: for future use
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.NeighborCellType)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE {param}')

	# noinspection PyTypeChecker
	def get_cnetwork(self) -> enums.CellsToMeasure:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:CNETwork \n
		Snippet: value: enums.CellsToMeasure = driver.configure.signaling.measurement.ueReport.ncell.result.get_cnetwork() \n
		Selects whether the UE must send measurement reports and for which neighbor cells. Applies only to <Type> = CNETwork, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
			:return: cells_to_measure: OFF: no neighbor cell measurement reports ALL: reporting for any neighbor cell LTE: LTE neighbor cells with licensed bands NRADio: NR neighbor cells LLAA: LTE neighbor cells with licensed or LAA bands LAA: LTE neighbor cells with LAA bands
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:CNETwork?')
		return Conversions.str_to_scalar_enum(response, enums.CellsToMeasure)

	def set_cnetwork(self, cells_to_measure: enums.CellsToMeasure) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:CNETwork \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.result.set_cnetwork(cells_to_measure = enums.CellsToMeasure.ALL) \n
		Selects whether the UE must send measurement reports and for which neighbor cells. Applies only to <Type> = CNETwork, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE \n
			:param cells_to_measure: OFF: no neighbor cell measurement reports ALL: reporting for any neighbor cell LTE: LTE neighbor cells with licensed bands NRADio: NR neighbor cells LLAA: LTE neighbor cells with licensed or LAA bands LAA: LTE neighbor cells with LAA bands
		"""
		param = Conversions.enum_scalar_to_str(cells_to_measure, enums.CellsToMeasure)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:CNETwork {param}')

	# noinspection PyTypeChecker
	def get_sib(self) -> enums.NcellsToMeasure:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:SIB \n
		Snippet: value: enums.NcellsToMeasure = driver.configure.signaling.measurement.ueReport.ncell.result.get_sib() \n
		Selects whether the UE must send measurement reports and for which neighbor cells. Applies only to <Type> = SIB, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE. \n
			:return: ncells_to_measure: OFF: no neighbor cell measurement reports ALL: reporting for all SIB neighbor cells IAFRequency: reporting intra-frequency SIB neighbor cells IFRequency: reporting inter-frequency SIB neighbor cells IRAT: reporting for inter-RAT SIB neighbor cells
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:SIB?')
		return Conversions.str_to_scalar_enum(response, enums.NcellsToMeasure)

	def set_sib(self, ncells_to_measure: enums.NcellsToMeasure) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:SIB \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.result.set_sib(ncells_to_measure = enums.NcellsToMeasure.ALL) \n
		Selects whether the UE must send measurement reports and for which neighbor cells. Applies only to <Type> = SIB, see
		[CONFigure:]SIGNaling:MEASurement:UEReport:NCELl:RESult:TYPE. \n
			:param ncells_to_measure: OFF: no neighbor cell measurement reports ALL: reporting for all SIB neighbor cells IAFRequency: reporting intra-frequency SIB neighbor cells IFRequency: reporting inter-frequency SIB neighbor cells IRAT: reporting for inter-RAT SIB neighbor cells
		"""
		param = Conversions.enum_scalar_to_str(ncells_to_measure, enums.NcellsToMeasure)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:SIB {param}')

	def get_nc_list(self) -> List[str]:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:NCList \n
		Snippet: value: List[str] = driver.configure.signaling.measurement.ueReport.ncell.result.get_nc_list() \n
		No command help available \n
			:return: cell_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:NCList?')
		return Conversions.str_to_str_list(response)

	def set_nc_list(self, cell_name: List[str]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:NCELl:RESult:NCList \n
		Snippet: driver.configure.signaling.measurement.ueReport.ncell.result.set_nc_list(cell_name = ['abc1', 'abc2', 'abc3']) \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.list_to_csv_quoted_str(cell_name)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:NCELl:RESult:NCList {param}')

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
