from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SendCls:
	"""Send commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("send", core, parent)

	def set(self, cell_name: str, ccrntis_end: enums.CcrntisEnd) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:SEND \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.ccrnti.send.set(cell_name = 'abc', ccrntis_end = enums.CcrntisEnd.ASF) \n
		Selects subframes for transmission of CC-RNTI, for fixed bursts. \n
			:param cell_name: No help available
			:param ccrntis_end: Send CC-RNTI: F2SF: final 2 SF LSF: last SF BLSF: before last SF SASF: skip all SF ASF: all SF
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ccrntis_end', ccrntis_end, DataType.Enum, enums.CcrntisEnd))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:SEND {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.CcrntisEnd:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:SEND \n
		Snippet: value: enums.CcrntisEnd = driver.configure.signaling.lte.cell.ueScheduling.laa.fburst.ccrnti.send.get(cell_name = 'abc') \n
		Selects subframes for transmission of CC-RNTI, for fixed bursts. \n
			:param cell_name: No help available
			:return: ccrntis_end: Send CC-RNTI: F2SF: final 2 SF LSF: last SF BLSF: before last SF SASF: skip all SF ASF: all SF"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:LAA:FBURst:CCRNti:SEND? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CcrntisEnd)
