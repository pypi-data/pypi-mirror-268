from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AaSchedulerCls:
	"""AaScheduler commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aaScheduler", core, parent)

	def set(self, cell_name: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:AASCheduler \n
		Snippet: driver.configure.signaling.nradio.cell.cdrx.aaScheduler.set(cell_name = 'abc', enable = False) \n
		Enables or disables automatic scheduling to ensure gaps for DRX opportunities. If connected DRX is disabled, this setting
		is ignored (implicit OFF) . Enable connected DRX via [CONFigure:]SIGNaling:NRADio:CELL:CDRX:ENABle. \n
			:param cell_name: No help available
			:param enable:
				- ON: The scheduler allocates DL resources only if there is DL data. Without queued DL data, no DL resources are allocated and there is an opportunity for DRX. In the UL direction, the scheduler allocates resources only upon request by the UE.
				- OFF: The configured scheduling applies."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:AASCheduler {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:AASCheduler \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.cdrx.aaScheduler.get(cell_name = 'abc') \n
		Enables or disables automatic scheduling to ensure gaps for DRX opportunities. If connected DRX is disabled, this setting
		is ignored (implicit OFF) . Enable connected DRX via [CONFigure:]SIGNaling:NRADio:CELL:CDRX:ENABle. \n
			:param cell_name: No help available
			:return: enable:
				- ON: The scheduler allocates DL resources only if there is DL data. Without queued DL data, no DL resources are allocated and there is an opportunity for DRX. In the UL direction, the scheduler allocates resources only upon request by the UE.
				- OFF: The configured scheduling applies."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:AASCheduler? {param}')
		return Conversions.str_to_bool(response)
