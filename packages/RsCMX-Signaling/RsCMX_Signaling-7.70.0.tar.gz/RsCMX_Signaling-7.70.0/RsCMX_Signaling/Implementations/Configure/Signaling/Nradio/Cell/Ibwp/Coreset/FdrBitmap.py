from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.Utilities import trim_str_response
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FdrBitmapCls:
	"""FdrBitmap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdrBitmap", core, parent)

	def set(self, cell_name: str, bitmap: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:COReset:FDRBitmap \n
		Snippet: driver.configure.signaling.nradio.cell.ibwp.coreset.fdrBitmap.set(cell_name = 'abc', bitmap = 'abc') \n
		Specifies the frequency domain resources for the CORESET 1, as a bitmap with 45 bits. \n
			:param cell_name: No help available
			:param bitmap: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('bitmap', bitmap, DataType.String))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:COReset:FDRBitmap {param}'.rstrip())

	def get(self, cell_name: str) -> str:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:COReset:FDRBitmap \n
		Snippet: value: str = driver.configure.signaling.nradio.cell.ibwp.coreset.fdrBitmap.get(cell_name = 'abc') \n
		Specifies the frequency domain resources for the CORESET 1, as a bitmap with 45 bits. \n
			:param cell_name: No help available
			:return: bitmap: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:COReset:FDRBitmap? {param}')
		return trim_str_response(response)
