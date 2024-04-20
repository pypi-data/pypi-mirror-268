from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LengthCls:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, cell_name: str, max_length: enums.MaxLength) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:MTB:LENGth \n
		Snippet: driver.configure.signaling.nradio.cell.dmrs.uplink.mtb.length.set(cell_name = 'abc', max_length = enums.MaxLength.L1) \n
		No command help available \n
			:param cell_name: No help available
			:param max_length: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('max_length', max_length, DataType.Enum, enums.MaxLength))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:MTB:LENGth {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.MaxLength:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:MTB:LENGth \n
		Snippet: value: enums.MaxLength = driver.configure.signaling.nradio.cell.dmrs.uplink.mtb.length.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: max_length: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:MTB:LENGth? {param}')
		return Conversions.str_to_scalar_enum(response, enums.MaxLength)
