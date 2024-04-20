from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, cell_name: str, frequency: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:FREQuency \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.uplink.frequency.set(cell_name = 'abc', frequency = 1.0) \n
		Defines the UL frequency. The DL frequency is not changed. \n
			:param cell_name: No help available
			:param frequency: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('frequency', frequency, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:FREQuency {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:FREQuency \n
		Snippet: value: float = driver.configure.signaling.lte.cell.rfSettings.uplink.frequency.get(cell_name = 'abc') \n
		Defines the UL frequency. The DL frequency is not changed. \n
			:param cell_name: No help available
			:return: frequency: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:FREQuency? {param}')
		return Conversions.str_to_float(response)
