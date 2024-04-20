from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpecialCls:
	"""Special commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("special", core, parent)

	def set(self, cell_name: str, special_pattern: enums.SpecialPattern) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TDD:SUBFrame:SPECial \n
		Snippet: driver.configure.signaling.lte.cell.tdd.subframe.special.set(cell_name = 'abc', special_pattern = enums.SpecialPattern.P0) \n
		Selects a special subframe pattern (SSP) for TDD, defining the inner structure of special subframes. \n
			:param cell_name: No help available
			:param special_pattern: P0 to P8: SSP 0 to SSP 8 P9: SSP 9 V1130 PAV1: SSP 10 V1430 PAV2: SSP 10 V1450 CRS Less DwPTS
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('special_pattern', special_pattern, DataType.Enum, enums.SpecialPattern))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:TDD:SUBFrame:SPECial {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.SpecialPattern:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TDD:SUBFrame:SPECial \n
		Snippet: value: enums.SpecialPattern = driver.configure.signaling.lte.cell.tdd.subframe.special.get(cell_name = 'abc') \n
		Selects a special subframe pattern (SSP) for TDD, defining the inner structure of special subframes. \n
			:param cell_name: No help available
			:return: special_pattern: P0 to P8: SSP 0 to SSP 8 P9: SSP 9 V1130 PAV1: SSP 10 V1430 PAV2: SSP 10 V1450 CRS Less DwPTS"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:TDD:SUBFrame:SPECial? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SpecialPattern)
