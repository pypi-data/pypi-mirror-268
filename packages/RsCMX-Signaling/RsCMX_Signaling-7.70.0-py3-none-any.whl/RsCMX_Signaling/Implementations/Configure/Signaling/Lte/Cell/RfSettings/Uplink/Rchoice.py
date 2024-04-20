from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RchoiceCls:
	"""Rchoice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rchoice", core, parent)

	def set(self, cell_name: str, range_choice: enums.RangeChoice) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:RCHoice \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.uplink.rchoice.set(cell_name = 'abc', range_choice = enums.RangeChoice.HASYmmetric) \n
		Selects a method for UL frequency configuration. \n
			:param cell_name: No help available
			:param range_choice: HASYmmetric refers to the high DL-only range, e.g. for band 66.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('range_choice', range_choice, DataType.Enum, enums.RangeChoice))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:RCHoice {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.RangeChoice:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:RCHoice \n
		Snippet: value: enums.RangeChoice = driver.configure.signaling.lte.cell.rfSettings.uplink.rchoice.get(cell_name = 'abc') \n
		Selects a method for UL frequency configuration. \n
			:param cell_name: No help available
			:return: range_choice: HASYmmetric refers to the high DL-only range, e.g. for band 66."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:RCHoice? {param}')
		return Conversions.str_to_scalar_enum(response, enums.RangeChoice)
