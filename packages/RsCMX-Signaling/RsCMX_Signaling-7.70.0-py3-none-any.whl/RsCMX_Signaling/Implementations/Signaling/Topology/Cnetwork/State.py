from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.StateCnetwork:
		"""SCPI: FETCh:SIGNaling:TOPology:CNETwork:STATe \n
		Snippet: value: enums.StateCnetwork = driver.signaling.topology.cnetwork.state.fetch() \n
		Queries the state of the core network, including the states 'edit mode' and 'live mode'. \n
			:return: state: NAV: No core network available. CREating: Creating the core network. IDLE: Core network available, edit mode. TESTing: Checking whether enough resources are available. EXHausted: Not enough resources to switch to live mode. STARting: Switching from edit mode to live mode. RUNNing: Live mode. STOPping: Switching from live mode to edit mode. DELeting: Deleting the core network. ERRor: Not recoverable core network error, delete or restart the core network."""
		response = self._core.io.query_str(f'FETCh:SIGNaling:TOPology:CNETwork:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.StateCnetwork)
