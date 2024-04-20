from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PbchCls:
	"""Pbch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pbch", core, parent)

	def set(self, cell_name: str, decibel: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:OFFSet:PBCH \n
		Snippet: driver.configure.signaling.lte.cell.power.downlink.offset.pbch.set(cell_name = 'abc', decibel = 1.0) \n
		Power level of the PBCH relative to the RS EPRE setting. \n
			:param cell_name: No help available
			:param decibel: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('decibel', decibel, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:OFFSet:PBCH {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:OFFSet:PBCH \n
		Snippet: value: float = driver.configure.signaling.lte.cell.power.downlink.offset.pbch.get(cell_name = 'abc') \n
		Power level of the PBCH relative to the RS EPRE setting. \n
			:param cell_name: No help available
			:return: decibel: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:OFFSet:PBCH? {param}')
		return Conversions.str_to_float(response)
