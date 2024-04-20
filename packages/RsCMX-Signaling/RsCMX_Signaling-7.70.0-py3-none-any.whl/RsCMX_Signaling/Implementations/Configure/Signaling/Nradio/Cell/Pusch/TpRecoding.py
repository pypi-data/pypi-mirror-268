from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpRecodingCls:
	"""TpRecoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpRecoding", core, parent)

	def set(self, cell_name: str, waveform: enums.Waveform) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TPRecoding \n
		Snippet: driver.configure.signaling.nradio.cell.pusch.tpRecoding.set(cell_name = 'abc', waveform = enums.Waveform.CP) \n
		Defines which type of OFDM the UE must use for the PUSCH, for the initial BWP. \n
			:param cell_name: No help available
			:param waveform: CP: CP-OFDM (no transform precoding) . DTFS: DFT-s-OFDM (with transform precoding) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('waveform', waveform, DataType.Enum, enums.Waveform))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TPRecoding {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Waveform:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TPRecoding \n
		Snippet: value: enums.Waveform = driver.configure.signaling.nradio.cell.pusch.tpRecoding.get(cell_name = 'abc') \n
		Defines which type of OFDM the UE must use for the PUSCH, for the initial BWP. \n
			:param cell_name: No help available
			:return: waveform: CP: CP-OFDM (no transform precoding) . DTFS: DFT-s-OFDM (with transform precoding) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TPRecoding? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Waveform)
