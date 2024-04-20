from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, cell_name: str, config_type: enums.ConfigType) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:MTB:TYPE \n
		Snippet: driver.configure.signaling.nradio.cell.dmrs.uplink.mtb.typePy.set(cell_name = 'abc', config_type = enums.ConfigType.T1) \n
		No command help available \n
			:param cell_name: No help available
			:param config_type: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('config_type', config_type, DataType.Enum, enums.ConfigType))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:MTB:TYPE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ConfigType:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:MTB:TYPE \n
		Snippet: value: enums.ConfigType = driver.configure.signaling.nradio.cell.dmrs.uplink.mtb.typePy.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: config_type: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:MTB:TYPE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ConfigType)
