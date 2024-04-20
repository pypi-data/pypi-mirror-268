from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReferenceCls:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, cell_name: str, ref_signal_power: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:REFerence \n
		Snippet: driver.configure.signaling.lte.cell.power.downlink.reference.set(cell_name = 'abc', ref_signal_power = 1.0) \n
		Configures the reference signal power. \n
			:param cell_name: No help available
			:param ref_signal_power: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ref_signal_power', ref_signal_power, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:REFerence {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:DL:REFerence \n
		Snippet: value: float = driver.configure.signaling.lte.cell.power.downlink.reference.get(cell_name = 'abc') \n
		Configures the reference signal power. \n
			:param cell_name: No help available
			:return: ref_signal_power: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:DL:REFerence? {param}')
		return Conversions.str_to_float(response)
