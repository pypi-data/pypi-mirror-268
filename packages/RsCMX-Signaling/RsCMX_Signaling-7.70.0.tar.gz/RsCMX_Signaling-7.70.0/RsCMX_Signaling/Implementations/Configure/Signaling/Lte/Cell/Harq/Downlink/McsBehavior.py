from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsBehaviorCls:
	"""McsBehavior commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsBehavior", core, parent)

	def set(self, cell_name: str, behavior: enums.McsBehavior) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:MCSBehavior \n
		Snippet: driver.configure.signaling.lte.cell.harq.downlink.mcsBehavior.set(cell_name = 'abc', behavior = enums.McsBehavior.AUTO) \n
		Defines the MCS selection for retransmissions. \n
			:param cell_name: No help available
			:param behavior: Automatic, substitute with ReTx MCS, repeat initial MCS, replace if invalid transport block.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('behavior', behavior, DataType.Enum, enums.McsBehavior))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:MCSBehavior {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.McsBehavior:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:MCSBehavior \n
		Snippet: value: enums.McsBehavior = driver.configure.signaling.lte.cell.harq.downlink.mcsBehavior.get(cell_name = 'abc') \n
		Defines the MCS selection for retransmissions. \n
			:param cell_name: No help available
			:return: behavior: Automatic, substitute with ReTx MCS, repeat initial MCS, replace if invalid transport block."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:MCSBehavior? {param}')
		return Conversions.str_to_scalar_enum(response, enums.McsBehavior)
