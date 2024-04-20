from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaddingCls:
	"""Padding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("padding", core, parent)

	def set(self, cell_name: str, padding: enums.SpsPadding, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:DL:PADDing \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.padding.set(cell_name = 'abc', padding = enums.SpsPadding.ALLZero, bwParts = repcap.BwParts.Default) \n
		Activates or deactivates downlink padding for SPS scheduling, for BWP <bb>. \n
			:param cell_name: No help available
			:param padding: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('padding', padding, DataType.Enum, enums.SpsPadding))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:DL:PADDing {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.SpsPadding:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:DL:PADDing \n
		Snippet: value: enums.SpsPadding = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.downlink.padding.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Activates or deactivates downlink padding for SPS scheduling, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: padding: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:DL:PADDing? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SpsPadding)
