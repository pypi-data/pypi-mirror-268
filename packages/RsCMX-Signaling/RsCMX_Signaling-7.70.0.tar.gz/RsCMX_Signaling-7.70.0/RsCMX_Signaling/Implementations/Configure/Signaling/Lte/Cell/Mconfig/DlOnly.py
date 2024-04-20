from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DlOnlyCls:
	"""DlOnly commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlOnly", core, parent)

	def set(self, cell_name: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:MCONfig:DLONly \n
		Snippet: driver.configure.signaling.lte.cell.mconfig.dlOnly.set(cell_name = 'abc', enable = False) \n
		Selects whether UL is forbidden for a cell in live mode. \n
			:param cell_name: No help available
			:param enable: ON: only DL OFF: UL and DL allowed
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:MCONfig:DLONly {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:MCONfig:DLONly \n
		Snippet: value: bool = driver.configure.signaling.lte.cell.mconfig.dlOnly.get(cell_name = 'abc') \n
		Selects whether UL is forbidden for a cell in live mode. \n
			:param cell_name: No help available
			:return: enable: ON: only DL OFF: UL and DL allowed"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:MCONfig:DLONly? {param}')
		return Conversions.str_to_bool(response)
