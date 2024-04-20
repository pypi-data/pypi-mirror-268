from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VcellCls:
	"""Vcell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vcell", core, parent)

	def set(self, cell_name: str, fbi: float = None, channel: float = None) -> None:
		"""SCPI: CREate:SIGNaling:LTE:VCELl \n
		Snippet: driver.create.signaling.lte.vcell.set(cell_name = 'abc', fbi = 1.0, channel = 1.0) \n
		Creates a virtual LTE cell. A virtual cell cannot be switched on. Assign a unique name to each named object within the
		test environment. Assigning an already used name can be rejected with an error message, even if the other object has not
		the same type as the new object. \n
			:param cell_name: Assigns a name to the cell. The string is used in other commands to select this cell.
			:param fbi: Frequency band indicator.
			:param channel: Channel number (EARFCN) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('fbi', fbi, DataType.Float, None, is_optional=True), ArgSingle('channel', channel, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CREate:SIGNaling:LTE:VCELl {param}'.rstrip())
