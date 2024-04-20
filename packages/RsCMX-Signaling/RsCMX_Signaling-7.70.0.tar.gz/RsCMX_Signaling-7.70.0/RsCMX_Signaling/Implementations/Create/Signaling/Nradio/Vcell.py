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

	def set(self, cell_name: str, fbi: int = None, channel: int = None) -> None:
		"""SCPI: CREate:SIGNaling:NRADio:VCELl \n
		Snippet: driver.create.signaling.nradio.vcell.set(cell_name = 'abc', fbi = 1, channel = 1) \n
		Creates a virtual NR cell. A virtual cell cannot be switched on. Assign a unique name to each named object within the
		test environment. Assigning an already used name can be rejected with an error message, even if the other object has not
		the same type as the new object. \n
			:param cell_name: Assigns a name to the cell. The string is used in other commands to select this cell.
			:param fbi: Frequency band indicator.
			:param channel: Channel number (NR ARFCN) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('fbi', fbi, DataType.Integer, None, is_optional=True), ArgSingle('channel', channel, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CREate:SIGNaling:NRADio:VCELl {param}'.rstrip())
