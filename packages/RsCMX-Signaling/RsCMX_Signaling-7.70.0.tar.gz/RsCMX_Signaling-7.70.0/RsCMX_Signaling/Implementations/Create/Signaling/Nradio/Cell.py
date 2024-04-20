from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def set(self, cell_name: str, physical_cell_id: int = None) -> None:
		"""SCPI: CREate:SIGNaling:NRADio:CELL \n
		Snippet: driver.create.signaling.nradio.cell.set(cell_name = 'abc', physical_cell_id = 1) \n
		The command creates a physical NR cell (a cell that can be switched on) . Assign a unique name to each named object
		within the test environment. Assigning an already used name can be rejected with an error message, even if the other
		object has not the same type as the new object. \n
			:param cell_name: Assigns a name to the cell. The string is used in other commands to select this cell.
			:param physical_cell_id: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('physical_cell_id', physical_cell_id, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CREate:SIGNaling:NRADio:CELL {param}'.rstrip())
