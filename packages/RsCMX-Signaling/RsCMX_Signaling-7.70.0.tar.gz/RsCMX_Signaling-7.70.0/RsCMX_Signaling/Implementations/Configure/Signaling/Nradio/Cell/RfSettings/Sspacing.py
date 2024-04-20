from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SspacingCls:
	"""Sspacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sspacing", core, parent)

	def set(self, cell_name: str, spacing: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:SSPacing \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.sspacing.set(cell_name = 'abc', spacing = 1) \n
		Selects the common subcarrier spacing of the cell. \n
			:param cell_name: No help available
			:param spacing: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('spacing', spacing, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:SSPacing {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:SSPacing \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.rfSettings.sspacing.get(cell_name = 'abc') \n
		Selects the common subcarrier spacing of the cell. \n
			:param cell_name: No help available
			:return: spacing: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:SSPacing? {param}')
		return Conversions.str_to_int(response)
