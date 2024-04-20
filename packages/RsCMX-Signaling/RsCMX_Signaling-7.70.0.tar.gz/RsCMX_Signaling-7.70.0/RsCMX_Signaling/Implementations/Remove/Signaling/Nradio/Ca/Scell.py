from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScellCls:
	"""Scell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scell", core, parent)

	def set(self, cell_group_name: str, cell_name: str) -> None:
		"""SCPI: REMove:SIGNaling:NRADio:CA:SCELl \n
		Snippet: driver.remove.signaling.nradio.ca.scell.set(cell_group_name = 'abc', cell_name = 'abc') \n
		Removes an LTE or NR cell from a cell group. \n
			:param cell_group_name: No help available
			:param cell_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_group_name', cell_group_name, DataType.String), ArgSingle('cell_name', cell_name, DataType.String))
		self._core.io.write(f'REMove:SIGNaling:NRADio:CA:SCELl {param}'.rstrip())
