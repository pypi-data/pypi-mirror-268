from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TbsBitsCls:
	"""TbsBits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbsBits", core, parent)

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:TBSBits \n
		Snippet: value: int = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.tbsBits.get(cell_name = 'abc') \n
		Queries the transport block size in bits for SPS UL scheduling. \n
			:param cell_name: No help available
			:return: tbs_bits: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:TBSBits? {param}')
		return Conversions.str_to_int(response)
