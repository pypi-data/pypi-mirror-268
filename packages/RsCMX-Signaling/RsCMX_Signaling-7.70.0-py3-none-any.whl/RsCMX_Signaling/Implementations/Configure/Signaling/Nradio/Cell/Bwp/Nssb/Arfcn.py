from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ArfcnCls:
	"""Arfcn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arfcn", core, parent)

	def set(self, cell_name: str, number: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:NSSB:ARFCn \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.nssb.arfcn.set(cell_name = 'abc', number = 1, bwParts = repcap.BwParts.Default) \n
		Configures the channel number of the NCD-SSB signaled as 'absoluteFrequencySSB-r17', for BWP <bb>. \n
			:param cell_name: No help available
			:param number: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('number', number, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:NSSB:ARFCn {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:NSSB:ARFCn \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.bwp.nssb.arfcn.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the channel number of the NCD-SSB signaled as 'absoluteFrequencySSB-r17', for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: number: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:NSSB:ARFCn? {param}')
		return Conversions.str_to_int(response)
