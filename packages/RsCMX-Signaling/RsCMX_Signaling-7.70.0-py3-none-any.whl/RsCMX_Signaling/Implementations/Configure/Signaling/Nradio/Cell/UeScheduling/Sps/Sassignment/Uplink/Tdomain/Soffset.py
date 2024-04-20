from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SoffsetCls:
	"""Soffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soffset", core, parent)

	def set(self, cell_name: str, offset: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:TDOMain:SOFFset \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.tdomain.soffset.set(cell_name = 'abc', offset = 1) \n
		Configures the slot offset k2 for the PUSCH, for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:param offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('offset', offset, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:TDOMain:SOFFset {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:TDOMain:SOFFset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.uplink.tdomain.soffset.get(cell_name = 'abc') \n
		Configures the slot offset k2 for the PUSCH, for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: offset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:UL:TDOMain:SOFFset? {param}')
		return Conversions.str_to_int(response)
