from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchFormatCls:
	"""PdcchFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcchFormat", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str, subframe: int) -> enums.PdcchFormat:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:PDCChformat \n
		Snippet: value: enums.PdcchFormat = driver.configure.signaling.lte.cell.ueScheduling.userDefined.sassignment.downlink.pdcchFormat.get(cell_name = 'abc', subframe = 1) \n
		Queries the number of CCEs used for transmission of the PDCCH, for the DL subframe with the index <Subframe>. \n
			:param cell_name: No help available
			:param subframe: No help available
			:return: pdcch_format: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('subframe', subframe, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:PDCChformat? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.PdcchFormat)
