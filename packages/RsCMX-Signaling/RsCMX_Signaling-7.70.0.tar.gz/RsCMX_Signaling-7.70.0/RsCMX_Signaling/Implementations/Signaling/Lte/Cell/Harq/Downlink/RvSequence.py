from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvSequenceCls:
	"""RvSequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvSequence", core, parent)

	def delete(self, cell_name: str, index: int, count: int = None) -> None:
		"""SCPI: DELete:SIGNaling:LTE:CELL:HARQ:DL:RVSequence \n
		Snippet: driver.signaling.lte.cell.harq.downlink.rvSequence.delete(cell_name = 'abc', index = 1, count = 1) \n
		Removes a block of entries from the RV sequences. \n
			:param cell_name: No help available
			:param index: Index of the first entry to be removed (lowest index is 0) .
			:param count: Number of entries to be removed (default is 1) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('count', count, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'DELete:SIGNaling:LTE:CELL:HARQ:DL:RVSequence {param}'.rstrip())
