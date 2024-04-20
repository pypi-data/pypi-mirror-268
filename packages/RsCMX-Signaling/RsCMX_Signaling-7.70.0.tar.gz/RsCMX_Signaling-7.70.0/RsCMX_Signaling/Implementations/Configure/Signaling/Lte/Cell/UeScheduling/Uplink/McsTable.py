from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsTableCls:
	"""McsTable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsTable", core, parent)

	def set(self, cell_name: str, mcs_table: enums.McsTableD) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:MCSTable \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.uplink.mcsTable.set(cell_name = 'abc', mcs_table = enums.McsTableD.Q16) \n
		Selects the maximum allowed UL modulation scheme. This selection indirectly selects an MCS table for mapping of the
		configured MCS values to modulation schemes and TBS indices. \n
			:param cell_name: No help available
			:param mcs_table: Max 16QAM, max 64QAM, max 256QAM
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs_table', mcs_table, DataType.Enum, enums.McsTableD))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:MCSTable {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.McsTableD:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UL:MCSTable \n
		Snippet: value: enums.McsTableD = driver.configure.signaling.lte.cell.ueScheduling.uplink.mcsTable.get(cell_name = 'abc') \n
		Selects the maximum allowed UL modulation scheme. This selection indirectly selects an MCS table for mapping of the
		configured MCS values to modulation schemes and TBS indices. \n
			:param cell_name: No help available
			:return: mcs_table: Max 16QAM, max 64QAM, max 256QAM"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UL:MCSTable? {param}')
		return Conversions.str_to_scalar_enum(response, enums.McsTableD)
