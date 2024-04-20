from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsageCls:
	"""Usage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usage", core, parent)

	def set(self, cell_name: str, schema: enums.Schema) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:USAGe \n
		Snippet: driver.configure.signaling.nradio.cell.srs.cnCodebook.usage.set(cell_name = 'abc', schema = enums.Schema.CODebook) \n
		Selects the usage of the SRS resource set for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
			:param schema: Codebook, non-codebook
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('schema', schema, DataType.Enum, enums.Schema))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:USAGe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Schema:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:CNCodebook:USAGe \n
		Snippet: value: enums.Schema = driver.configure.signaling.nradio.cell.srs.cnCodebook.usage.get(cell_name = 'abc') \n
		Selects the usage of the SRS resource set for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
			:return: schema: Codebook, non-codebook"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SRS:CNCodebook:USAGe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Schema)
