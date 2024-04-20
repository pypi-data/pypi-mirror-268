from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, cell_name: str) -> enums.StatePwrControl:
		"""SCPI: FETCh:SIGNaling:NRADio:CELL:POWer:CONTrol:STATe \n
		Snippet: value: enums.StatePwrControl = driver.signaling.nradio.cell.power.control.state.fetch(cell_name = 'abc') \n
		Queries whether a TPC power control procedure is running for the initial BWP. For example, whether commanding the UE to
		maximum power is still ongoing or already complete. \n
			:param cell_name: No help available
			:return: state: Ready or running"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'FETCh:SIGNaling:NRADio:CELL:POWer:CONTrol:STATe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.StatePwrControl)
