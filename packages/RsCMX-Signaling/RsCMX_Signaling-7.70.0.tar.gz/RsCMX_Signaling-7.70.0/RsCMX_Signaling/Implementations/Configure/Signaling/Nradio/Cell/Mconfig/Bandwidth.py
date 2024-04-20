from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, cell_name: str, bandwidth: enums.DlUlBandwidth) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:BWIDth \n
		Snippet: driver.configure.signaling.nradio.cell.mconfig.bandwidth.set(cell_name = 'abc', bandwidth = enums.DlUlBandwidth.B005) \n
		Selects the maximum carrier bandwidth allowed in live mode. \n
			:param cell_name: No help available
			:param bandwidth: Bandwidth in MHz
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('bandwidth', bandwidth, DataType.Enum, enums.DlUlBandwidth))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:BWIDth {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.DlUlBandwidth:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:BWIDth \n
		Snippet: value: enums.DlUlBandwidth = driver.configure.signaling.nradio.cell.mconfig.bandwidth.get(cell_name = 'abc') \n
		Selects the maximum carrier bandwidth allowed in live mode. \n
			:param cell_name: No help available
			:return: bandwidth: Bandwidth in MHz"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:BWIDth? {param}')
		return Conversions.str_to_scalar_enum(response, enums.DlUlBandwidth)
