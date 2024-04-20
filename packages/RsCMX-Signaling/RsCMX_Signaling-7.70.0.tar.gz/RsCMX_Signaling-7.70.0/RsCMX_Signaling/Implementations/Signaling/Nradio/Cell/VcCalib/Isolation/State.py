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
		"""SCPI: FETCh:SIGNaling:NRADio:CELL:VCCalib:ISOLation:STATe \n
		Snippet: value: enums.StatePwrControl = driver.signaling.nradio.cell.vcCalib.isolation.state.fetch(cell_name = 'abc') \n
		Queries the state of the procedure updating the isolation quality. \n
			:param cell_name: No help available
			:return: state: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'FETCh:SIGNaling:NRADio:CELL:VCCalib:ISOLation:STATe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.StatePwrControl)
