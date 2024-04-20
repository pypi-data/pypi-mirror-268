from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlevelCls:
	"""Alevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alevel", core, parent)

	def set(self, cell_name: str, level: enums.Level) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:DL:ALEVel \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.downlink.alevel.set(cell_name = 'abc', level = enums.Level.AL1) \n
		Specifies the aggregation level for the DL, for the initial BWP. \n
			:param cell_name: No help available
			:param level: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('level', level, DataType.Enum, enums.Level))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:DL:ALEVel {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Level:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:DL:ALEVel \n
		Snippet: value: enums.Level = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.downlink.alevel.get(cell_name = 'abc') \n
		Specifies the aggregation level for the DL, for the initial BWP. \n
			:param cell_name: No help available
			:return: level: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:DL:ALEVel? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Level)
