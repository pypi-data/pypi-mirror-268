from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsOrderCls:
	"""PsOrder commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psOrder", core, parent)

	def set(self, cell_name: str, order: enums.PsOrder) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:PSORder \n
		Snippet: driver.configure.signaling.lte.cell.harq.downlink.psOrder.set(cell_name = 'abc', order = enums.PsOrder.RROBin) \n
		Defines the scheduling order of the HARQ processes. \n
			:param cell_name: No help available
			:param order: Round robin or subframe bound
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('order', order, DataType.Enum, enums.PsOrder))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:PSORder {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PsOrder:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:PSORder \n
		Snippet: value: enums.PsOrder = driver.configure.signaling.lte.cell.harq.downlink.psOrder.get(cell_name = 'abc') \n
		Defines the scheduling order of the HARQ processes. \n
			:param cell_name: No help available
			:return: order: Round robin or subframe bound"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:PSORder? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PsOrder)
