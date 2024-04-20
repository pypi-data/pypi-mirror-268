from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	def set(self, name_ta_eps: str, name_cell: str) -> None:
		"""SCPI: REMove:SIGNaling:TOPology:EPS \n
		Snippet: driver.remove.signaling.topology.eps.set(name_ta_eps = 'abc', name_cell = 'abc') \n
		Removes the link between a cell and an EPS tracking area. \n
			:param name_ta_eps: No help available
			:param name_cell: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta_eps', name_ta_eps, DataType.String), ArgSingle('name_cell', name_cell, DataType.String))
		self._core.io.write(f'REMove:SIGNaling:TOPology:EPS {param}'.rstrip())
