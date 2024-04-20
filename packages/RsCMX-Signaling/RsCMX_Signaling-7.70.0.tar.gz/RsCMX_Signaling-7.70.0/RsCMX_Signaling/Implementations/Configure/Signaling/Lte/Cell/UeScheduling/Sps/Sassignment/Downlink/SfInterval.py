from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfIntervalCls:
	"""SfInterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfInterval", core, parent)

	def set(self, cell_name: str, sf_interval: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:SFINterval \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.downlink.sfInterval.set(cell_name = 'abc', sf_interval = 1) \n
		Selects the subframe periodicity for SPS DL scheduling. \n
			:param cell_name: No help available
			:param sf_interval: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('sf_interval', sf_interval, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:SFINterval {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:SFINterval \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.downlink.sfInterval.get(cell_name = 'abc') \n
		Selects the subframe periodicity for SPS DL scheduling. \n
			:param cell_name: No help available
			:return: sf_interval: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:SFINterval? {param}')
		return Conversions.str_to_int(response)
