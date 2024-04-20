from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnoRepetCls:
	"""PnoRepet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnoRepet", core, parent)

	def set(self, cell_name: str, slot: int, repetitions: enums.Repetitions) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:PNORepet \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.uplink.tdomain.pnoRepet.set(cell_name = 'abc', slot = 1, repetitions = enums.Repetitions.N12) \n
		Specifies the number of PUSCH repetitions signaled as 'numberOfRepetitions', for the UL slot with the index <Slot>, for
		the initial BWP. Prerequisite: Configure [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PRTYpe. \n
			:param cell_name: No help available
			:param slot: No help available
			:param repetitions: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer), ArgSingle('repetitions', repetitions, DataType.Enum, enums.Repetitions))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:PNORepet {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, slot: int) -> enums.Repetitions:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:PNORepet \n
		Snippet: value: enums.Repetitions = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.uplink.tdomain.pnoRepet.get(cell_name = 'abc', slot = 1) \n
		Specifies the number of PUSCH repetitions signaled as 'numberOfRepetitions', for the UL slot with the index <Slot>, for
		the initial BWP. Prerequisite: Configure [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PRTYpe. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: repetitions: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:UL:TDOMain:PNORepet? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.Repetitions)
