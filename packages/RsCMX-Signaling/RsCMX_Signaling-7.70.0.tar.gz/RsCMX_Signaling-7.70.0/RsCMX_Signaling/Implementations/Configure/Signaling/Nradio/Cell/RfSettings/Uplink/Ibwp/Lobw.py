from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LobwCls:
	"""Lobw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lobw", core, parent)

	def set(self, cell_name: str, lobw: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:UL:IBWP:LOBW \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.uplink.ibwp.lobw.set(cell_name = 'abc', lobw = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param lobw: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('lobw', lobw, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:UL:IBWP:LOBW {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:UL:IBWP:LOBW \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.rfSettings.uplink.ibwp.lobw.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: lobw: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:UL:IBWP:LOBW? {param}')
		return Conversions.str_to_int(response)
