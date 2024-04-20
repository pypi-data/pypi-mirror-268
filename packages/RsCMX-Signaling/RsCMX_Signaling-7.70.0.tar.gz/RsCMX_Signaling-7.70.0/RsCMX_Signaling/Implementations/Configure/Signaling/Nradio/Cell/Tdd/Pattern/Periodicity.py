from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, cell_name: str, periodicity: enums.Periodicity, pattern=repcap.Pattern.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TDD:PATTern<PatternNo>:PERiodicity \n
		Snippet: driver.configure.signaling.nradio.cell.tdd.pattern.periodicity.set(cell_name = 'abc', periodicity = enums.Periodicity.P0P5, pattern = repcap.Pattern.Default) \n
		Configures the periodicity of the UL-DL pattern {p}. \n
			:param cell_name: No help available
			:param periodicity: Periodicity, 0.5 ms (P0P5) to 10 ms (P10) .
			:param pattern: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Enum, enums.Periodicity))
		pattern_cmd_val = self._cmd_group.get_repcap_cmd_value(pattern, repcap.Pattern)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:TDD:PATTern{pattern_cmd_val}:PERiodicity {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, pattern=repcap.Pattern.Default) -> enums.Periodicity:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TDD:PATTern<PatternNo>:PERiodicity \n
		Snippet: value: enums.Periodicity = driver.configure.signaling.nradio.cell.tdd.pattern.periodicity.get(cell_name = 'abc', pattern = repcap.Pattern.Default) \n
		Configures the periodicity of the UL-DL pattern {p}. \n
			:param cell_name: No help available
			:param pattern: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
			:return: periodicity: Periodicity, 0.5 ms (P0P5) to 10 ms (P10) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		pattern_cmd_val = self._cmd_group.get_repcap_cmd_value(pattern, repcap.Pattern)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:TDD:PATTern{pattern_cmd_val}:PERiodicity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Periodicity)
