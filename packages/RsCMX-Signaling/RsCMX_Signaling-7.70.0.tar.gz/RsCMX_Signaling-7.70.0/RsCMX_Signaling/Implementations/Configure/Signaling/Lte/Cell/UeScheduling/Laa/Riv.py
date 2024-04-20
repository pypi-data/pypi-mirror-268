from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RivCls:
	"""Riv commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("riv", core, parent)

	def set(self, cell_name: str, subframe: int, riv: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RIV \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.riv.set(cell_name = 'abc', subframe = 1, riv = 1) \n
		Configures the resource indication value (RIV) for LAA subframes with <Subframe> allocated symbols. \n
			:param cell_name: No help available
			:param subframe: No help available
			:param riv: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer), ArgSingle('riv', riv, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RIV {param}'.rstrip())

	def get(self, cell_name: str, subframe: int) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:RIV \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.laa.riv.get(cell_name = 'abc', subframe = 1) \n
		Configures the resource indication value (RIV) for LAA subframes with <Subframe> allocated symbols. \n
			:param cell_name: No help available
			:param subframe: No help available
			:return: riv: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:RIV? {param}'.rstrip())
		return Conversions.str_to_int(response)
