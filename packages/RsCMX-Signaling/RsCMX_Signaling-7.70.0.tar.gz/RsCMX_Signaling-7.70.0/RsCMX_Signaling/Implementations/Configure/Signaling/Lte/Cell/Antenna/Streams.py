from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StreamsCls:
	"""Streams commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("streams", core, parent)

	def set(self, cell_name: str, dl_iq_data_streams: enums.DlIqDataStreams) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ANTenna:STReams \n
		Snippet: driver.configure.signaling.lte.cell.antenna.streams.set(cell_name = 'abc', dl_iq_data_streams = enums.DlIqDataStreams.S1) \n
		Sets the number of I/Q data streams. \n
			:param cell_name: No help available
			:param dl_iq_data_streams: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('dl_iq_data_streams', dl_iq_data_streams, DataType.Enum, enums.DlIqDataStreams))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:ANTenna:STReams {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.DlIqDataStreams:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ANTenna:STReams \n
		Snippet: value: enums.DlIqDataStreams = driver.configure.signaling.lte.cell.antenna.streams.get(cell_name = 'abc') \n
		Sets the number of I/Q data streams. \n
			:param cell_name: No help available
			:return: dl_iq_data_streams: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:ANTenna:STReams? {param}')
		return Conversions.str_to_scalar_enum(response, enums.DlIqDataStreams)
