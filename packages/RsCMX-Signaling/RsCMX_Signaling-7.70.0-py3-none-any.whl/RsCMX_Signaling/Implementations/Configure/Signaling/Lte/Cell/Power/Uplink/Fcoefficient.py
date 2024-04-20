from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FcoefficientCls:
	"""Fcoefficient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcoefficient", core, parent)

	def set(self, cell_name: str, filter_coeff: enums.FilterCoeff) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:FCOefficient \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.fcoefficient.set(cell_name = 'abc', filter_coeff = enums.FilterCoeff.FC0) \n
		Sets the parameter 'filterCoefficient', signaled to the UE as an uplink power control parameter. \n
			:param cell_name: No help available
			:param filter_coeff: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('filter_coeff', filter_coeff, DataType.Enum, enums.FilterCoeff))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:FCOefficient {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FilterCoeff:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:FCOefficient \n
		Snippet: value: enums.FilterCoeff = driver.configure.signaling.lte.cell.power.uplink.fcoefficient.get(cell_name = 'abc') \n
		Sets the parameter 'filterCoefficient', signaled to the UE as an uplink power control parameter. \n
			:param cell_name: No help available
			:return: filter_coeff: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:FCOefficient? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FilterCoeff)
