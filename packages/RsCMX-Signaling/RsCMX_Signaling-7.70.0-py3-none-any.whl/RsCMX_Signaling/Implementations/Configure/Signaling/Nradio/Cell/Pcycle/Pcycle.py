from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcycleCls:
	"""Pcycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcycle", core, parent)

	def set(self, cell_name: str, paging_cycle: enums.PagingCycle) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PCYCle:PCYCle \n
		Snippet: driver.configure.signaling.nradio.cell.pcycle.pcycle.set(cell_name = 'abc', paging_cycle = enums.PagingCycle.P128) \n
		Selects the paging cycle in radio frames. \n
			:param cell_name: No help available
			:param paging_cycle: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('paging_cycle', paging_cycle, DataType.Enum, enums.PagingCycle))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PCYCle:PCYCle {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PagingCycle:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PCYCle:PCYCle \n
		Snippet: value: enums.PagingCycle = driver.configure.signaling.nradio.cell.pcycle.pcycle.get(cell_name = 'abc') \n
		Selects the paging cycle in radio frames. \n
			:param cell_name: No help available
			:return: paging_cycle: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PCYCle:PCYCle? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PagingCycle)
