from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TdBehaviorCls:
	"""TdBehavior commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdBehavior", core, parent)

	def set(self, cell_name: str, td_behavior: enums.TdType, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:TDBehavior \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.srs.cnCodebook.tdBehavior.set(cell_name = 'abc', td_behavior = enums.TdType.APERiodic, bwParts = repcap.BwParts.Default) \n
		Selects the time domain behavior ('resourceType') of the SRS resource set and thus enables or disables periodic SRS, for
		BWP <bb>. \n
			:param cell_name: No help available
			:param td_behavior: APERiodic: no SRS transmissions PERiodic: SRS transmissions in every nth slot
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('td_behavior', td_behavior, DataType.Enum, enums.TdType))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:TDBehavior {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.TdType:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:TDBehavior \n
		Snippet: value: enums.TdType = driver.configure.signaling.nradio.cell.bwp.srs.cnCodebook.tdBehavior.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the time domain behavior ('resourceType') of the SRS resource set and thus enables or disables periodic SRS, for
		BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: td_behavior: APERiodic: no SRS transmissions PERiodic: SRS transmissions in every nth slot"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:TDBehavior? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TdType)
