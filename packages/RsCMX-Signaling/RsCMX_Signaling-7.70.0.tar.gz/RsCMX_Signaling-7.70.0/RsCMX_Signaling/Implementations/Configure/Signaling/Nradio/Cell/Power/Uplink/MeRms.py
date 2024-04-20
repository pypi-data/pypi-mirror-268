from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeRmsCls:
	"""MeRms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("meRms", core, parent)

	def set(self, cell_name: str, power: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:MERMs \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.meRms.set(cell_name = 'abc', power = 1.0) \n
		Defines the maximum expected RMS UL power, for user-defined configuration. For automatic configuration, you can query the
		value. \n
			:param cell_name: No help available
			:param power: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('power', power, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:MERMs {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:MERMs \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.power.uplink.meRms.get(cell_name = 'abc') \n
		Defines the maximum expected RMS UL power, for user-defined configuration. For automatic configuration, you can query the
		value. \n
			:param cell_name: No help available
			:return: power: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:MERMs? {param}')
		return Conversions.str_to_float(response)
