from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcellCls:
	"""Ncell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncell", core, parent)

	def set(self, cell_name: str, ncell_name: str) -> None:
		"""SCPI: REMove:SIGNaling:LTE:NCELl \n
		Snippet: driver.remove.signaling.lte.ncell.set(cell_name = 'abc', ncell_name = 'abc') \n
		Removes a cell from the SIB neighbor cell list of an LTE or NR cell. \n
			:param cell_name: Name of the cell for which the neighbor is removed.
			:param ncell_name: Name of the neighbor cell.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ncell_name', ncell_name, DataType.String))
		self._core.io.write(f'REMove:SIGNaling:LTE:NCELl {param}'.rstrip())
