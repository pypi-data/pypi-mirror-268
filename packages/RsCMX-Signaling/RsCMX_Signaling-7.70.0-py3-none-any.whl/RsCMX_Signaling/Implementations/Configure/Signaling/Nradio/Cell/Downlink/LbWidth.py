from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LbWidthCls:
	"""LbWidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lbWidth", core, parent)

	def set(self, cell_name: str, riv: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DL:LBWidth \n
		Snippet: driver.configure.signaling.nradio.cell.downlink.lbWidth.set(cell_name = 'abc', riv = 1) \n
		Defines the resource indication value (RIV) signaled as 'locationAndBandwidth', for the downlink, for the initial BWP. \n
			:param cell_name: No help available
			:param riv: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('riv', riv, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:DL:LBWidth {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DL:LBWidth \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.downlink.lbWidth.get(cell_name = 'abc') \n
		Defines the resource indication value (RIV) signaled as 'locationAndBandwidth', for the downlink, for the initial BWP. \n
			:param cell_name: No help available
			:return: riv: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:DL:LBWidth? {param}')
		return Conversions.str_to_int(response)
