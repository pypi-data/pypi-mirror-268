from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsageCls:
	"""Usage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usage", core, parent)

	def set(self, cell_name: str, schema: enums.Schema, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:USAGe \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.srs.cnCodebook.usage.set(cell_name = 'abc', schema = enums.Schema.CODebook, bwParts = repcap.BwParts.Default) \n
		Selects the usage of the SRS resource set for periodic SRS, for BWP <bb>. \n
			:param cell_name: No help available
			:param schema: Codebook, non-codebook
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('schema', schema, DataType.Enum, enums.Schema))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:USAGe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Schema:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:USAGe \n
		Snippet: value: enums.Schema = driver.configure.signaling.nradio.cell.bwp.srs.cnCodebook.usage.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the usage of the SRS resource set for periodic SRS, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: schema: Codebook, non-codebook"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:USAGe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Schema)
