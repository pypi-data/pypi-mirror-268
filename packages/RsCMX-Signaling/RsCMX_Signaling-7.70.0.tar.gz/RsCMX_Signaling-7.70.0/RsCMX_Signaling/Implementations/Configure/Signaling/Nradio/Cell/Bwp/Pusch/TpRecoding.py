from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpRecodingCls:
	"""TpRecoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpRecoding", core, parent)

	def set(self, cell_name: str, waveform: enums.Waveform, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TPRecoding \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.pusch.tpRecoding.set(cell_name = 'abc', waveform = enums.Waveform.CP, bwParts = repcap.BwParts.Default) \n
		Defines which type of OFDM the UE must use for the PUSCH, for BWP <bb>. \n
			:param cell_name: No help available
			:param waveform: CP: CP-OFDM (no transform precoding) . DTFS: DFT-s-OFDM (with transform precoding) .
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('waveform', waveform, DataType.Enum, enums.Waveform))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TPRecoding {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Waveform:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TPRecoding \n
		Snippet: value: enums.Waveform = driver.configure.signaling.nradio.cell.bwp.pusch.tpRecoding.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines which type of OFDM the UE must use for the PUSCH, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: waveform: CP: CP-OFDM (no transform precoding) . DTFS: DFT-s-OFDM (with transform precoding) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TPRecoding? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Waveform)
