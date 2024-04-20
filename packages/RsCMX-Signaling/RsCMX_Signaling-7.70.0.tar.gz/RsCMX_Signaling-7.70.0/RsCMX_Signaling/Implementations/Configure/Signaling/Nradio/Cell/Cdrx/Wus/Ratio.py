from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RatioCls:
	"""Ratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ratio", core, parent)

	def set(self, cell_name: str, ratio_on_off: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:WUS:RATio \n
		Snippet: driver.configure.signaling.nradio.cell.cdrx.wus.ratio.set(cell_name = 'abc', ratio_on_off = 1.0) \n
		Configures the percentage of long DRX cycles for which the UE is woken up via DCI with format 2-6 containing wake-up
		indication = 1. \n
			:param cell_name: No help available
			:param ratio_on_off: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ratio_on_off', ratio_on_off, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:WUS:RATio {param}'.rstrip())

	def get(self, cell_name: str) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:WUS:RATio \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.cdrx.wus.ratio.get(cell_name = 'abc') \n
		Configures the percentage of long DRX cycles for which the UE is woken up via DCI with format 2-6 containing wake-up
		indication = 1. \n
			:param cell_name: No help available
			:return: ratio_on_off: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:WUS:RATio? {param}')
		return Conversions.str_to_float(response)
