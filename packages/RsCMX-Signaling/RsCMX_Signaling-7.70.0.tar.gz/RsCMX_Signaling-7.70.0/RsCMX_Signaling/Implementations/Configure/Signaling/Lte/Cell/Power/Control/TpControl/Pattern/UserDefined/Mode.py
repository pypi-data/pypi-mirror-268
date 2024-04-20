from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.Repeat) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:MODE \n
		Snippet: driver.configure.signaling.lte.cell.power.control.tpControl.pattern.userDefined.mode.set(cell_name = 'abc', mode = enums.Repeat.CONTinuous) \n
		Selects the mode for execution of a user-defined TPC pattern. \n
			:param cell_name: No help available
			:param mode: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.Repeat))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Repeat:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:MODE \n
		Snippet: value: enums.Repeat = driver.configure.signaling.lte.cell.power.control.tpControl.pattern.userDefined.mode.get(cell_name = 'abc') \n
		Selects the mode for execution of a user-defined TPC pattern. \n
			:param cell_name: No help available
			:return: mode: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl:PATTern:UDEFined:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)
