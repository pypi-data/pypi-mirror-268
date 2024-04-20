from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciFormatCls:
	"""DciFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciFormat", core, parent)

	def set(self, cell_name: str, slot: int, dci_format: enums.DciFormatB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:DCIFormat \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.dciFormat.set(cell_name = 'abc', slot = 1, dci_format = enums.DciFormatB.D10) \n
		Defines the DCI format for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:param dci_format: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer), ArgSingle('dci_format', dci_format, DataType.Enum, enums.DciFormatB))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:DCIFormat {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, slot: int) -> enums.DciFormatB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:DCIFormat \n
		Snippet: value: enums.DciFormatB = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.dciFormat.get(cell_name = 'abc', slot = 1) \n
		Defines the DCI format for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: dci_format: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:DCIFormat? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.DciFormatB)
