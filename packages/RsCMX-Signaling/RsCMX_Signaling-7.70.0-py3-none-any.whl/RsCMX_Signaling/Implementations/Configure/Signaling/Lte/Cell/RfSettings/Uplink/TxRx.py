from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxRxCls:
	"""TxRx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txRx", core, parent)

	def set(self, cell_name: str, tx_rx_separation: enums.TxRxSeparation) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:TXRX \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.uplink.txRx.set(cell_name = 'abc', tx_rx_separation = enums.TxRxSeparation.DEFault) \n
		Selects a configuration method for the uplink carrier center frequency, for FDD. \n
			:param cell_name: No help available
			:param tx_rx_separation: UDEFined: Define UL frequency independent of DL frequency. DEFault: Use standardized UL-DL separation.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('tx_rx_separation', tx_rx_separation, DataType.Enum, enums.TxRxSeparation))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:TXRX {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.TxRxSeparation:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:TXRX \n
		Snippet: value: enums.TxRxSeparation = driver.configure.signaling.lte.cell.rfSettings.uplink.txRx.get(cell_name = 'abc') \n
		Selects a configuration method for the uplink carrier center frequency, for FDD. \n
			:param cell_name: No help available
			:return: tx_rx_separation: UDEFined: Define UL frequency independent of DL frequency. DEFault: Use standardized UL-DL separation."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:TXRX? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TxRxSeparation)
