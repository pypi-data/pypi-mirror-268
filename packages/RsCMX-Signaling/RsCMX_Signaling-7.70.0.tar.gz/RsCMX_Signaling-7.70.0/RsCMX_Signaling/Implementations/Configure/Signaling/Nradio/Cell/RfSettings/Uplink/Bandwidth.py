from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, cell_name: str, bandwidth: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:UL:BWIDth \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.uplink.bandwidth.set(cell_name = 'abc', bandwidth = 1.0) \n
		Selects the carrier bandwidth for the uplink. \n
			:param cell_name: No help available
			:param bandwidth: Numeric value in Hz or enumerated value in MHz.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('bandwidth', bandwidth, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:UL:BWIDth {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:UL:BWIDth \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.rfSettings.uplink.bandwidth.get(cell_name = 'abc') \n
		Selects the carrier bandwidth for the uplink. \n
			:param cell_name: No help available
			:return: bandwidth: Numeric value in Hz or enumerated value in MHz."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:UL:BWIDth? {param}')
		return Conversions.str_to_float(response)
