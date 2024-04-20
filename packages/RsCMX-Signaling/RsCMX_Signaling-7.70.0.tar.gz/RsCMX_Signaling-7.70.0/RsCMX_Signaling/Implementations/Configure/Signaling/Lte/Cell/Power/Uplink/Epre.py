from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpreCls:
	"""Epre commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("epre", core, parent)

	def set(self, cell_name: str, max_exp_erpe: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:EPRE \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.epre.set(cell_name = 'abc', max_exp_erpe = 1.0) \n
		Sets the maximum EPRE expected in the UL, for user-defined configuration. For automatic configuration, you can query the
		value. \n
			:param cell_name: No help available
			:param max_exp_erpe: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('max_exp_erpe', max_exp_erpe, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:EPRE {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:EPRE \n
		Snippet: value: float = driver.configure.signaling.lte.cell.power.uplink.epre.get(cell_name = 'abc') \n
		Sets the maximum EPRE expected in the UL, for user-defined configuration. For automatic configuration, you can query the
		value. \n
			:param cell_name: No help available
			:return: max_exp_erpe: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:EPRE? {param}')
		return Conversions.str_to_float(response)
