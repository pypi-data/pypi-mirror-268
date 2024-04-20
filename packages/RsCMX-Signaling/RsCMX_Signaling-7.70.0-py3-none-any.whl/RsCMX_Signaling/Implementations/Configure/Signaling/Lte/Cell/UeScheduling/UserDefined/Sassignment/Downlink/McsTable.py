from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsTableCls:
	"""McsTable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsTable", core, parent)

	def set(self, cell_name: str, mcs_table: enums.McsTable) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:MCSTable \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.mcsTable.set(cell_name = 'abc', mcs_table = enums.McsTable.Q1K) \n
		Selects the maximum allowed DL modulation scheme. This selection indirectly selects an MCS table for mapping of the
		configured MCS values to modulation schemes and TBS indices. \n
			:param cell_name: No help available
			:param mcs_table: Max 64QAM, max 256QAM, max 1024QAM
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs_table', mcs_table, DataType.Enum, enums.McsTable))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:MCSTable {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.McsTable:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:MCSTable \n
		Snippet: value: enums.McsTable = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.mcsTable.get(cell_name = 'abc') \n
		Selects the maximum allowed DL modulation scheme. This selection indirectly selects an MCS table for mapping of the
		configured MCS values to modulation schemes and TBS indices. \n
			:param cell_name: No help available
			:return: mcs_table: Max 64QAM, max 256QAM, max 1024QAM"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:MCSTable? {param}')
		return Conversions.str_to_scalar_enum(response, enums.McsTable)
