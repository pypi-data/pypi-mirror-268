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
	def fetch(self) -> enums.State:
		"""SCPI: FETCh:SIGNaling:MEASurement:CQIReporting:STATe \n
		Snippet: value: enums.State = driver.signaling.measurement.cqiReporting.state.fetch() \n
		Queries the measurement state. \n
			:return: state: OFF: Measurement off, no results. RDY: Measurement finished, valid results can be available. RUN: Measurement running."""
		response = self._core.io.query_str(f'FETCh:SIGNaling:MEASurement:CQIReporting:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.State)
