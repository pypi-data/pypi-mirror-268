from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PositionCls:
	"""Position commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def set(self, cell_name: str, position: enums.MtxPosition, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:DMRS:UL:MTA:POSition \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.dmrs.uplink.mta.position.set(cell_name = 'abc', position = enums.MtxPosition.P0, bwParts = repcap.BwParts.Default) \n
		Defines parameter 'dmrs-AdditionalPosition' for PUSCH, mapping type A, BWP <bb>. \n
			:param cell_name: No help available
			:param position: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('position', position, DataType.Enum, enums.MtxPosition))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:DMRS:UL:MTA:POSition {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.MtxPosition:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:DMRS:UL:MTA:POSition \n
		Snippet: value: enums.MtxPosition = driver.configure.signaling.nradio.cell.bwp.dmrs.uplink.mta.position.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines parameter 'dmrs-AdditionalPosition' for PUSCH, mapping type A, BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: position: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:DMRS:UL:MTA:POSition? {param}')
		return Conversions.str_to_scalar_enum(response, enums.MtxPosition)
