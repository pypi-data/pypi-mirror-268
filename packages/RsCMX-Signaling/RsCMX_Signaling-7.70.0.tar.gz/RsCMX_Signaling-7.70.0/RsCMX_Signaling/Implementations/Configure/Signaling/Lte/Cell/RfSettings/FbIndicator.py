from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FbIndicatorCls:
	"""FbIndicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fbIndicator", core, parent)

	def set(self, cell_name: str, fbi: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:FBINdicator \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.fbIndicator.set(cell_name = 'abc', fbi = 1) \n
		Defines the frequency band. \n
			:param cell_name: No help available
			:param fbi: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('fbi', fbi, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:FBINdicator {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:FBINdicator \n
		Snippet: value: int = driver.configure.signaling.lte.cell.rfSettings.fbIndicator.get(cell_name = 'abc') \n
		Defines the frequency band. \n
			:param cell_name: No help available
			:return: fbi: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:FBINdicator? {param}')
		return Conversions.str_to_int(response)
