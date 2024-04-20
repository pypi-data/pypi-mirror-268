from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScellCls:
	"""Scell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scell", core, parent)

	def set(self, cell_group_name: str, cell_name: List[str], activation: List[bool] = None, ul_enable: List[enums.UlEnable] = None) -> None:
		"""SCPI: ADD:SIGNaling:NRADio:CA:SCELl \n
		Snippet: driver.add.signaling.nradio.ca.scell.set(cell_group_name = 'abc', cell_name = ['abc1', 'abc2', 'abc3'], activation = [True, False, True], ul_enable = [UlEnable.OFF, UlEnable.SRS]) \n
		Adds one or more existing NR cells to an existing cell group, with the role SCell. \n
			:param cell_group_name: No help available
			:param cell_name: No help available
			:param activation: ON: automatic MAC activation (default) OFF: manual MAC activation via separate command
			:param ul_enable: OFF: The SCell has no uplink. ON: The SCell has an uplink with PUSCH. SRS: PUSCH-less SCell with SRS, for SRS carrier switching.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_group_name', cell_group_name, DataType.String), ArgSingle.as_open_list('cell_name', cell_name, DataType.StringList, None), ArgSingle('activation', activation, DataType.BooleanList, None, True, True, 1), ArgSingle('ul_enable', ul_enable, DataType.EnumList, enums.UlEnable, True, True, 1))
		self._core.io.write(f'ADD:SIGNaling:NRADio:CA:SCELl {param}'.rstrip())
