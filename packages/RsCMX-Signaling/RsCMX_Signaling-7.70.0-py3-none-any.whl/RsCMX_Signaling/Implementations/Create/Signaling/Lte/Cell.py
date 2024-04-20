from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def set(self, cell_name: str, preferred_netw: enums.PreferredNetw = None, physical_cell_id: float = None) -> None:
		"""SCPI: CREate:SIGNaling:LTE:CELL \n
		Snippet: driver.create.signaling.lte.cell.set(cell_name = 'abc', preferred_netw = enums.PreferredNetw.AUTO, physical_cell_id = 1.0) \n
		Creates a physical LTE cell (a cell that can be switched on) . Assign a unique name to each named object within the test
		environment. Assigning an already used name can be rejected with an error message, even if the other object has not the
		same type as the new object. \n
			:param cell_name: Assigns a name to the cell. The string is used in other commands to select this cell.
			:param preferred_netw: No help available
			:param physical_cell_id: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('preferred_netw', preferred_netw, DataType.Enum, enums.PreferredNetw, is_optional=True), ArgSingle('physical_cell_id', physical_cell_id, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CREate:SIGNaling:LTE:CELL {param}'.rstrip())
