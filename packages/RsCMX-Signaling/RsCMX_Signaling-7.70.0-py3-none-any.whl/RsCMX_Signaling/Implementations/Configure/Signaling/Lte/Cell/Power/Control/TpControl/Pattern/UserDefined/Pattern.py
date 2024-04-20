from typing import List

from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, cell_name: str, pattern: List[enums.Pattern]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:PATTern \n
		Snippet: driver.configure.signaling.lte.cell.power.control.tpControl.pattern.userDefined.pattern.set(cell_name = 'abc', pattern = [Pattern.D1, Pattern.U3]) \n
		Configures a user-defined TPC pattern as a sequence of commands. \n
			:param cell_name: No help available
			:param pattern: Comma-separated list of commands D1: -1 dB KEEP: 0 dB U1: +1 dB U3: +3 dB A single NAV is returned if no pattern is defined.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle.as_open_list('pattern', pattern, DataType.EnumList, enums.Pattern))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> List[enums.Pattern]:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:PATTern \n
		Snippet: value: List[enums.Pattern] = driver.configure.signaling.lte.cell.power.control.tpControl.pattern.userDefined.pattern.get(cell_name = 'abc') \n
		Configures a user-defined TPC pattern as a sequence of commands. \n
			:param cell_name: No help available
			:return: pattern: Comma-separated list of commands D1: -1 dB KEEP: 0 dB U1: +1 dB U3: +3 dB A single NAV is returned if no pattern is defined."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:PATTern? {param}')
		return Conversions.str_to_list_enum(response, enums.Pattern)
