from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PssCls:
	"""Pss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pss", core, parent)

	def set(self, cell_name: str, pss: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:POFFset:PSS \n
		Snippet: driver.configure.signaling.nradio.cell.power.downlink.poffset.pss.set(cell_name = 'abc', pss = 1) \n
		Defines the offset of the PSS power relative to the SSS power. \n
			:param cell_name: No help available
			:param pss: 0: PSS EPRE = SSS EPRE 3: PSS EPRE = SSS EPRE + 3 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('pss', pss, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:POFFset:PSS {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:POFFset:PSS \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.power.downlink.poffset.pss.get(cell_name = 'abc') \n
		Defines the offset of the PSS power relative to the SSS power. \n
			:param cell_name: No help available
			:return: pss: 0: PSS EPRE = SSS EPRE 3: PSS EPRE = SSS EPRE + 3 dB"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:POFFset:PSS? {param}')
		return Conversions.str_to_int(response)
