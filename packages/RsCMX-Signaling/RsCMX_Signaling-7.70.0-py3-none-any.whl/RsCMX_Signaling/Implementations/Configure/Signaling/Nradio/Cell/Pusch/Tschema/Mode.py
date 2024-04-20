from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, choice: enums.Choice) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TSCHema:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.pusch.tschema.mode.set(cell_name = 'abc', choice = enums.Choice.CODebook) \n
		Selects the PUSCH transmission scheme, signaled as 'txConfig', for the initial BWP. \n
			:param cell_name: No help available
			:param choice: SINGle: single antenna port, 'txConfig' not signaled CODebook: codebook-based transmission NCODebook: currently not supported
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('choice', choice, DataType.Enum, enums.Choice))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TSCHema:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Choice:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TSCHema:MODE \n
		Snippet: value: enums.Choice = driver.configure.signaling.nradio.cell.pusch.tschema.mode.get(cell_name = 'abc') \n
		Selects the PUSCH transmission scheme, signaled as 'txConfig', for the initial BWP. \n
			:param cell_name: No help available
			:return: choice: SINGle: single antenna port, 'txConfig' not signaled CODebook: codebook-based transmission NCODebook: currently not supported"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TSCHema:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Choice)
