from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsepreCls:
	"""Rsepre commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsepre", core, parent)

	def set(self, cell_name: str, rs_erpe: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:RSEPre \n
		Snippet: driver.configure.signaling.lte.cell.power.downlink.rsepre.set(cell_name = 'abc', rs_erpe = 1.0) \n
		Defines the energy per resource element (EPRE) of the cell-specific reference signal (C-RS) . \n
			:param cell_name: No help available
			:param rs_erpe: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('rs_erpe', rs_erpe, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:RSEPre {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:RSEPre \n
		Snippet: value: float = driver.configure.signaling.lte.cell.power.downlink.rsepre.get(cell_name = 'abc') \n
		Defines the energy per resource element (EPRE) of the cell-specific reference signal (C-RS) . \n
			:param cell_name: No help available
			:return: rs_erpe: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:RSEPre? {param}')
		return Conversions.str_to_float(response)
