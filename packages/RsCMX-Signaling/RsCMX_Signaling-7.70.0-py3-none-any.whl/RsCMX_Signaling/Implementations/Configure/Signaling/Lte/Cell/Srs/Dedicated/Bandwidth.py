from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, cell_name: str, bandwidth: enums.BandwidthDedicated) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:SRS:DEDicated:BWIDth \n
		Snippet: driver.configure.signaling.lte.cell.srs.dedicated.bandwidth.set(cell_name = 'abc', bandwidth = enums.BandwidthDedicated.BW0) \n
		Configures the parameter 'srs-Bandwidth'. Only configurable for the mode UDEFined. \n
			:param cell_name: No help available
			:param bandwidth: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('bandwidth', bandwidth, DataType.Enum, enums.BandwidthDedicated))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:SRS:DEDicated:BWIDth {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.BandwidthDedicated:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:SRS:DEDicated:BWIDth \n
		Snippet: value: enums.BandwidthDedicated = driver.configure.signaling.lte.cell.srs.dedicated.bandwidth.get(cell_name = 'abc') \n
		Configures the parameter 'srs-Bandwidth'. Only configurable for the mode UDEFined. \n
			:param cell_name: No help available
			:return: bandwidth: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:SRS:DEDicated:BWIDth? {param}')
		return Conversions.str_to_scalar_enum(response, enums.BandwidthDedicated)
