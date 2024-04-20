from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrateCls:
	"""Crate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crate", core, parent)

	def get(self, cell_name: str, subframe: int) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:CRATe \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.laa.crate.get(cell_name = 'abc', subframe = 1) \n
		Queries the code rate for LAA subframes with <Subframe> allocated symbols. \n
			:param cell_name: No help available
			:param subframe: No help available
			:return: modulation: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:CRATe? {param}'.rstrip())
		return Conversions.str_to_int(response)
