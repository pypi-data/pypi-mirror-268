from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RblocksCls:
	"""Rblocks commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rblocks", core, parent)

	def set(self, cell_name: str, resource_blocks: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:RBLocks \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.uplink.rblocks.set(cell_name = 'abc', resource_blocks = 1) \n
		Selects the number of uplink RBs for full allocation and thus the uplink channel bandwidth. Configure the same value for
		DL and UL. \n
			:param cell_name: No help available
			:param resource_blocks: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_blocks', resource_blocks, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:RBLocks {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:RBLocks \n
		Snippet: value: int = driver.configure.signaling.lte.cell.rfSettings.uplink.rblocks.get(cell_name = 'abc') \n
		Selects the number of uplink RBs for full allocation and thus the uplink channel bandwidth. Configure the same value for
		DL and UL. \n
			:param cell_name: No help available
			:return: resource_blocks: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:RBLocks? {param}')
		return Conversions.str_to_int(response)
