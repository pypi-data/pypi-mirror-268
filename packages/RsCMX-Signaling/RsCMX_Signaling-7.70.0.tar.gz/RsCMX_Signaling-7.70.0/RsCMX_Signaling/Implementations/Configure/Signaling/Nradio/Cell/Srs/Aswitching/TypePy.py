from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, cell_name: str, type_py: enums.AswitchingType) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:ASWitching:TYPE \n
		Snippet: driver.configure.signaling.nradio.cell.srs.aswitching.typePy.set(cell_name = 'abc', type_py = enums.AswitchingType.T1R1) \n
		Selects the antenna switching resource type for the initial BWP. \n
			:param cell_name: No help available
			:param type_py: TtRr defines the number of ports t per SRS resource and the total number of ports over all SRS resources r.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('type_py', type_py, DataType.Enum, enums.AswitchingType))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:ASWitching:TYPE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.AswitchingType:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:ASWitching:TYPE \n
		Snippet: value: enums.AswitchingType = driver.configure.signaling.nradio.cell.srs.aswitching.typePy.get(cell_name = 'abc') \n
		Selects the antenna switching resource type for the initial BWP. \n
			:param cell_name: No help available
			:return: type_py: TtRr defines the number of ports t per SRS resource and the total number of ports over all SRS resources r."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SRS:ASWitching:TYPE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.AswitchingType)
