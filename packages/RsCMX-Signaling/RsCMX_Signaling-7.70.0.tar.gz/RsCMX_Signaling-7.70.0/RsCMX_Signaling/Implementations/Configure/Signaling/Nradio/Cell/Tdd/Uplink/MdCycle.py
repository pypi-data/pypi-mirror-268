from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MdCycleCls:
	"""MdCycle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mdCycle", core, parent)

	def set(self, cell_name: str, ul_max_duty_cyle: enums.UlMaxDutyCyle) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TDD:UL:MDCYcle \n
		Snippet: driver.configure.signaling.nradio.cell.tdd.uplink.mdCycle.set(cell_name = 'abc', ul_max_duty_cyle = enums.UlMaxDutyCyle.D80) \n
		Configures the maximum percentage of scheduled UL symbols. Selecting a D8x value also configures other settings so that
		they are compatible to maximum UL duty cycle tests. \n
			:param cell_name: No help available
			:param ul_max_duty_cyle: OFF: no maximum duty cycle applied D80 | D82 | D85 | D87: 80 % to 87 % D89: 89.6 %
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ul_max_duty_cyle', ul_max_duty_cyle, DataType.Enum, enums.UlMaxDutyCyle))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:TDD:UL:MDCYcle {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.UlMaxDutyCyle:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:TDD:UL:MDCYcle \n
		Snippet: value: enums.UlMaxDutyCyle = driver.configure.signaling.nradio.cell.tdd.uplink.mdCycle.get(cell_name = 'abc') \n
		Configures the maximum percentage of scheduled UL symbols. Selecting a D8x value also configures other settings so that
		they are compatible to maximum UL duty cycle tests. \n
			:param cell_name: No help available
			:return: ul_max_duty_cyle: OFF: no maximum duty cycle applied D80 | D82 | D85 | D87: 80 % to 87 % D89: 89.6 %"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:TDD:UL:MDCYcle? {param}')
		return Conversions.str_to_scalar_enum(response, enums.UlMaxDutyCyle)
