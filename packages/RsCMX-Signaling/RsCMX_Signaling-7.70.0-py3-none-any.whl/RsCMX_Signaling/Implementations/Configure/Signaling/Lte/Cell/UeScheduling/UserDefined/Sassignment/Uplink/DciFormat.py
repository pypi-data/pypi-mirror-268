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

	def set(self, cell_name: str, subframe: int, dci_format: enums.DciFormat) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:DCIFormat \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.uplink.dciFormat.set(cell_name = 'abc', subframe = 1, dci_format = enums.DciFormat.D0) \n
		Defines the DCI format for the UL subframe with the index <Subframe>. \n
			:param cell_name: No help available
			:param subframe: No help available
			:param dci_format: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer), ArgSingle('dci_format', dci_format, DataType.Enum, enums.DciFormat))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:DCIFormat {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, subframe: int) -> enums.DciFormat:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:DCIFormat \n
		Snippet: value: enums.DciFormat = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.uplink.dciFormat.get(cell_name = 'abc', subframe = 1) \n
		Defines the DCI format for the UL subframe with the index <Subframe>. \n
			:param cell_name: No help available
			:param subframe: No help available
			:return: dci_format: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:UL:DCIFormat? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.DciFormat)
