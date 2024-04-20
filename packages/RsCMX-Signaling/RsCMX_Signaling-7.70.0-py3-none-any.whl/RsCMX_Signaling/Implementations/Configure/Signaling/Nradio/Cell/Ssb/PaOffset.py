from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaOffsetCls:
	"""PaOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("paOffset", core, parent)

	def set(self, cell_name: str, offset: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:PAOFfset \n
		Snippet: driver.configure.signaling.nradio.cell.ssb.paOffset.set(cell_name = 'abc', offset = 1) \n
		Defines the parameter 'offsetToPointA' of the SIB. \n
			:param cell_name: No help available
			:param offset: Number of RB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('offset', offset, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SSB:PAOFfset {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:PAOFfset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ssb.paOffset.get(cell_name = 'abc') \n
		Defines the parameter 'offsetToPointA' of the SIB. \n
			:param cell_name: No help available
			:return: offset: Number of RB"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:SSB:PAOFfset? {param}')
		return Conversions.str_to_int(response)
