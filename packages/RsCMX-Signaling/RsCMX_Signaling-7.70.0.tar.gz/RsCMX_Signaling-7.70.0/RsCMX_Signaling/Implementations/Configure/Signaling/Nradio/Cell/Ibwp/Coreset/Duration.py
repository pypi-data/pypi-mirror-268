from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DurationCls:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, cell_name: str, duration: enums.Spreset) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:COReset:DURation \n
		Snippet: driver.configure.signaling.nradio.cell.ibwp.coreset.duration.set(cell_name = 'abc', duration = enums.Spreset.S1) \n
		Specifies the duration of the CORESET 1, in PDCCH symbols. \n
			:param cell_name: No help available
			:param duration: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('duration', duration, DataType.Enum, enums.Spreset))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:COReset:DURation {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Spreset:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:COReset:DURation \n
		Snippet: value: enums.Spreset = driver.configure.signaling.nradio.cell.ibwp.coreset.duration.get(cell_name = 'abc') \n
		Specifies the duration of the CORESET 1, in PDCCH symbols. \n
			:param cell_name: No help available
			:return: duration: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:COReset:DURation? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Spreset)
