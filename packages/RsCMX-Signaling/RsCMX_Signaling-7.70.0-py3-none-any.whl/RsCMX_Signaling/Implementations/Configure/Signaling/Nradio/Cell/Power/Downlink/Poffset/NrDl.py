from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrDlCls:
	"""NrDl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrDl", core, parent)

	def set(self, cell_name: str, nr_dl: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:POFFset:NRDL \n
		Snippet: driver.configure.signaling.nradio.cell.power.downlink.poffset.nrDl.set(cell_name = 'abc', nr_dl = 1.0) \n
		Defines the offset of the DL power (PDSCH) relative to the SSS power. \n
			:param cell_name: No help available
			:param nr_dl: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('nr_dl', nr_dl, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:POFFset:NRDL {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:POFFset:NRDL \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.power.downlink.poffset.nrDl.get(cell_name = 'abc') \n
		Defines the offset of the DL power (PDSCH) relative to the SSS power. \n
			:param cell_name: No help available
			:return: nr_dl: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:POFFset:NRDL? {param}')
		return Conversions.str_to_float(response)
