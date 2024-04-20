from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnoRepetCls:
	"""PnoRepet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnoRepet", core, parent)

	def set(self, cell_name: str, repetitions: enums.Repetitions) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PNORepet \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.pnoRepet.set(cell_name = 'abc', repetitions = enums.Repetitions.N12) \n
		No command help available \n
			:param cell_name: No help available
			:param repetitions: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('repetitions', repetitions, DataType.Enum, enums.Repetitions))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PNORepet {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Repetitions:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PNORepet \n
		Snippet: value: enums.Repetitions = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.pnoRepet.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: repetitions: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PNORepet? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Repetitions)
