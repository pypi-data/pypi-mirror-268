from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, cell_name: str, enable: bool, pattern=repcap.Pattern.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TDD:PATTern<PatternNo>:ENABle \n
		Snippet: driver.configure.signaling.nradio.cell.tdd.pattern.enable.set(cell_name = 'abc', enable = False, pattern = repcap.Pattern.Default) \n
		Enables or disables the second UL-DL pattern. \n
			:param cell_name: No help available
			:param enable: No help available
			:param pattern: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		pattern_cmd_val = self._cmd_group.get_repcap_cmd_value(pattern, repcap.Pattern)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:TDD:PATTern{pattern_cmd_val}:ENABle {param}'.rstrip())

	def get(self, cell_name: str, pattern=repcap.Pattern.Default) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TDD:PATTern<PatternNo>:ENABle \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.tdd.pattern.enable.get(cell_name = 'abc', pattern = repcap.Pattern.Default) \n
		Enables or disables the second UL-DL pattern. \n
			:param cell_name: No help available
			:param pattern: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pattern')
			:return: enable: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		pattern_cmd_val = self._cmd_group.get_repcap_cmd_value(pattern, repcap.Pattern)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:TDD:PATTern{pattern_cmd_val}:ENABle? {param}')
		return Conversions.str_to_bool(response)
