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

	def set(self, cell_name: str, mcs: enums.McsTableB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:DTFS:MCSTable \n
		Snippet: driver.configure.signaling.nradio.cell.pusch.dtfs.mcsTable.set(cell_name = 'abc', mcs = enums.McsTableB.L64) \n
		Defines which MCS table must be used for PUSCH with transform precoding (parameter 'mcs-TableTransformPrecoder') , for
		the initial BWP. \n
			:param cell_name: No help available
			:param mcs: 256QAM, 64QAM low SE, 64QAM
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs', mcs, DataType.Enum, enums.McsTableB))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:DTFS:MCSTable {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.McsTableB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:DTFS:MCSTable \n
		Snippet: value: enums.McsTableB = driver.configure.signaling.nradio.cell.pusch.dtfs.mcsTable.get(cell_name = 'abc') \n
		Defines which MCS table must be used for PUSCH with transform precoding (parameter 'mcs-TableTransformPrecoder') , for
		the initial BWP. \n
			:param cell_name: No help available
			:return: mcs: 256QAM, 64QAM low SE, 64QAM"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:DTFS:MCSTable? {param}')
		return Conversions.str_to_scalar_enum(response, enums.McsTableB)
