from typing import List

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

	def set(self, cell_group_name: str, cell_name: List[str], activation: List[bool] = None, ul_enable: List[bool] = None) -> None:
		"""SCPI: ADD:SIGNaling:LTE:CA:SCELl \n
		Snippet: driver.add.signaling.lte.ca.scell.set(cell_group_name = 'abc', cell_name = ['abc1', 'abc2', 'abc3'], activation = [True, False, True], ul_enable = [True, False, True]) \n
		Adds one or more existing LTE cells to an existing cell group, with the role SCell. \n
			:param cell_group_name: No help available
			:param cell_name: No help available
			:param activation: ON: automatic MAC activation (default) OFF: manual MAC activation via separate command
			:param ul_enable: Enables the UL (UL carrier aggregation) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_group_name', cell_group_name, DataType.String), ArgSingle.as_open_list('cell_name', cell_name, DataType.StringList, None), ArgSingle('activation', activation, DataType.BooleanList, None, True, True, 1), ArgSingle('ul_enable', ul_enable, DataType.BooleanList, None, True, True, 1))
		self._core.io.write(f'ADD:SIGNaling:LTE:CA:SCELl {param}'.rstrip())
