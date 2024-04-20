from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SframeCls:
	"""Sframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sframe", core, parent)

	def set(self, cell_name: str, subframe: enums.Subframe) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:SRS:COMMon:SFRame \n
		Snippet: driver.configure.signaling.lte.cell.srs.common.sframe.set(cell_name = 'abc', subframe = enums.Subframe.SC0) \n
		Configures the parameter 'srs-SubframeConfig'. Only configurable for the mode UDEFined. \n
			:param cell_name: No help available
			:param subframe: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Enum, enums.Subframe))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:SRS:COMMon:SFRame {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Subframe:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:SRS:COMMon:SFRame \n
		Snippet: value: enums.Subframe = driver.configure.signaling.lte.cell.srs.common.sframe.get(cell_name = 'abc') \n
		Configures the parameter 'srs-SubframeConfig'. Only configurable for the mode UDEFined. \n
			:param cell_name: No help available
			:return: subframe: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:SRS:COMMon:SFRame? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Subframe)
