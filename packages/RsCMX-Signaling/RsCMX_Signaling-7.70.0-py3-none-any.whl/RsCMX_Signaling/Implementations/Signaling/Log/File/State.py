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
	def fetch(self) -> enums.LogFileState:
		"""SCPI: FETCh:SIGNaling:LOG:FILE:STATe \n
		Snippet: value: enums.LogFileState = driver.signaling.log.file.state.fetch() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'FETCh:SIGNaling:LOG:FILE:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.LogFileState)
