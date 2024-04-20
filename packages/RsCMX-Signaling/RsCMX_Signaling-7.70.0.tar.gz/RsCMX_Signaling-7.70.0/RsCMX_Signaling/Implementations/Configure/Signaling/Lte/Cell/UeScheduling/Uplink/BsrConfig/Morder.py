from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MorderCls:
	"""Morder commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("morder", core, parent)

	def set(self, cell_name: str, order: enums.ModulationOrder) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MORDer \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.uplink.bsrConfig.morder.set(cell_name = 'abc', order = enums.ModulationOrder.Q16) \n
		Selects the maximum modulation scheme for follow BSR, MCS configuration mode MMO. \n
			:param cell_name: No help available
			:param order: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('order', order, DataType.Enum, enums.ModulationOrder))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MORDer {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModulationOrder:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MORDer \n
		Snippet: value: enums.ModulationOrder = driver.configure.signaling.lte.cell.ueScheduling.uplink.bsrConfig.morder.get(cell_name = 'abc') \n
		Selects the maximum modulation scheme for follow BSR, MCS configuration mode MMO. \n
			:param cell_name: No help available
			:return: order: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:BSRConfig:MORDer? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModulationOrder)
