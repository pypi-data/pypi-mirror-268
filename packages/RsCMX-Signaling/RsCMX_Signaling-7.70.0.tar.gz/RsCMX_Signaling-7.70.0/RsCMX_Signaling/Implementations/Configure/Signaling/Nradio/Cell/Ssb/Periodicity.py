from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, cell_name: str, periodicity: enums.PeriodicityB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:PERiodicity \n
		Snippet: driver.configure.signaling.nradio.cell.ssb.periodicity.set(cell_name = 'abc', periodicity = enums.PeriodicityB.P10) \n
		Selects the periodicity of the SSB in the time domain. \n
			:param cell_name: No help available
			:param periodicity: Periodicity in ms (5 ms to 160 ms)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Enum, enums.PeriodicityB))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SSB:PERiodicity {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PeriodicityB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:PERiodicity \n
		Snippet: value: enums.PeriodicityB = driver.configure.signaling.nradio.cell.ssb.periodicity.get(cell_name = 'abc') \n
		Selects the periodicity of the SSB in the time domain. \n
			:param cell_name: No help available
			:return: periodicity: Periodicity in ms (5 ms to 160 ms)"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SSB:PERiodicity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PeriodicityB)
