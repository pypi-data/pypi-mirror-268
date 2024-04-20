from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LbWidthCls:
	"""LbWidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lbWidth", core, parent)

	def set(self, cell_name: str, riv: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwpid>:UL:LBWidth \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.uplink.lbWidth.set(cell_name = 'abc', riv = 1, bwParts = repcap.BwParts.Default) \n
		Defines the resource indication value (RIV) signaled as 'locationAndBandwidth', for the uplink, for BWP <bb>. \n
			:param cell_name: No help available
			:param riv: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('riv', riv, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UL:LBWidth {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwpid>:UL:LBWidth \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.bwp.uplink.lbWidth.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines the resource indication value (RIV) signaled as 'locationAndBandwidth', for the uplink, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: riv: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UL:LBWidth? {param}')
		return Conversions.str_to_int(response)
