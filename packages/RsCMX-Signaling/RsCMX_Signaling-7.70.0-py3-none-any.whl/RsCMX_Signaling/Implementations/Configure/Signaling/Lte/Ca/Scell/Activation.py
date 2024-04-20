from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ActivationCls:
	"""Activation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("activation", core, parent)

	def set(self, cell_name: List[str], activation: List[bool]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CA:SCELl:ACTivation \n
		Snippet: driver.configure.signaling.lte.ca.scell.activation.set(cell_name = ['abc1', 'abc2', 'abc3'], activation = [True, False, True]) \n
		Triggers the manual MAC activation or MAC deactivation for an SCell or several SCells. A query returns the current MAC
		activation state for an SCell. \n
			:param cell_name: No help available
			:param activation: ON: Activate MAC (setting) / MAC is active (query) . OFF: Deactivate MAC (setting) / MAC is inactive (query) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('cell_name', cell_name, DataType.StringList, None), ArgSingle.as_open_list('activation', activation, DataType.BooleanList, None))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CA:SCELl:ACTivation {param}'.rstrip())

	def get(self, cell_name: List[str]) -> List[bool]:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CA:SCELl:ACTivation \n
		Snippet: value: List[bool] = driver.configure.signaling.lte.ca.scell.activation.get(cell_name = ['abc1', 'abc2', 'abc3']) \n
		Triggers the manual MAC activation or MAC deactivation for an SCell or several SCells. A query returns the current MAC
		activation state for an SCell. \n
			:param cell_name: No help available
			:return: activation: ON: Activate MAC (setting) / MAC is active (query) . OFF: Deactivate MAC (setting) / MAC is inactive (query) ."""
		param = Conversions.list_to_csv_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CA:SCELl:ACTivation? {param}')
		return Conversions.str_to_bool_list(response)
