from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpEnableCls:
	"""TpEnable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpEnable", core, parent)

	def set(self, cell_name: str, enable_tp: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:TPENable \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.tpEnable.set(cell_name = 'abc', enable_tp = False) \n
		Configures the signaled 'transformPrecoder' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:param enable_tp: ON: DFT-s-OFDM (with transform precoding) . OFF: CP-OFDM (no transform precoding) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable_tp', enable_tp, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:TPENable {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:TPENable \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.tpEnable.get(cell_name = 'abc') \n
		Configures the signaled 'transformPrecoder' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: enable_tp: ON: DFT-s-OFDM (with transform precoding) . OFF: CP-OFDM (no transform precoding) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:TPENable? {param}')
		return Conversions.str_to_bool(response)
