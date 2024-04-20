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

	def set(self, cell_name: str, pdcch_format: enums.PdcchFormatB) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:PDCChformat \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.ccrnti.pdcchFormat.set(cell_name = 'abc', pdcch_format = enums.PdcchFormatB.N1) \n
		Selects the number of control channel elements (CCE) used for transmission of the PDCCH scrambled with CC-RNTI, for fixed
		bursts. \n
			:param cell_name: No help available
			:param pdcch_format: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('pdcch_format', pdcch_format, DataType.Enum, enums.PdcchFormatB))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:PDCChformat {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PdcchFormatB:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:PDCChformat \n
		Snippet: value: enums.PdcchFormatB = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.ccrnti.pdcchFormat.get(cell_name = 'abc') \n
		Selects the number of control channel elements (CCE) used for transmission of the PDCCH scrambled with CC-RNTI, for fixed
		bursts. \n
			:param cell_name: No help available
			:return: pdcch_format: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:PDCChformat? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PdcchFormatB)
