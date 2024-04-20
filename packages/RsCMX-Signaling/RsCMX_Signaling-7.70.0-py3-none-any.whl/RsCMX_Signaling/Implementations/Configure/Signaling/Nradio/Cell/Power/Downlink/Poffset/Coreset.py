from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CoresetCls:
	"""Coreset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coreset", core, parent)

	def set(self, cell_name: str, coreset: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:POFFset:COReset \n
		Snippet: driver.configure.signaling.nradio.cell.power.downlink.poffset.coreset.set(cell_name = 'abc', coreset = 1.0) \n
		Defines the offset of the CORESET power relative to the SSS power. \n
			:param cell_name: No help available
			:param coreset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('coreset', coreset, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:POFFset:COReset {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:POFFset:COReset \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.power.downlink.poffset.coreset.get(cell_name = 'abc') \n
		Defines the offset of the CORESET power relative to the SSS power. \n
			:param cell_name: No help available
			:return: coreset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:POFFset:COReset? {param}')
		return Conversions.str_to_float(response)
