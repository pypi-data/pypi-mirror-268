from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, cell_name: str, pattern: enums.RpPattern) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:PATTern \n
		Snippet: driver.configure.signaling.nradio.cell.power.control.tpControl.rpTolerance.pattern.set(cell_name = 'abc', pattern = enums.RpPattern.A) \n
		Selects a TPC pattern for ramping up and ramping down relative power tolerance tests, for the initial BWP. \n
			:param cell_name: No help available
			:param pattern: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('pattern', pattern, DataType.Enum, enums.RpPattern))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:PATTern {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.RpPattern:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:PATTern \n
		Snippet: value: enums.RpPattern = driver.configure.signaling.nradio.cell.power.control.tpControl.rpTolerance.pattern.get(cell_name = 'abc') \n
		Selects a TPC pattern for ramping up and ramping down relative power tolerance tests, for the initial BWP. \n
			:param cell_name: No help available
			:return: pattern: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:PATTern? {param}')
		return Conversions.str_to_scalar_enum(response, enums.RpPattern)
