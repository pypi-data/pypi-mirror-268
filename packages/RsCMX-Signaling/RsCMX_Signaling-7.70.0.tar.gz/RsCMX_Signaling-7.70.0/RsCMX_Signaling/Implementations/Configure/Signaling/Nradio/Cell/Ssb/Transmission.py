from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TransmissionCls:
	"""Transmission commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transmission", core, parent)

	def set(self, cell_name: str, burst_trx: enums.AutoMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:TRANsmission \n
		Snippet: driver.configure.signaling.nradio.cell.ssb.transmission.set(cell_name = 'abc', burst_trx = enums.AutoMode.AUTO) \n
		No command help available \n
			:param cell_name: No help available
			:param burst_trx: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('burst_trx', burst_trx, DataType.Enum, enums.AutoMode))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SSB:TRANsmission {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.AutoMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:TRANsmission \n
		Snippet: value: enums.AutoMode = driver.configure.signaling.nradio.cell.ssb.transmission.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: burst_trx: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SSB:TRANsmission? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
