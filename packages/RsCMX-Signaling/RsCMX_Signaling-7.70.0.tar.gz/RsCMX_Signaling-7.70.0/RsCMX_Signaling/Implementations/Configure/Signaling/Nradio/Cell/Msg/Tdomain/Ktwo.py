from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class KtwoCls:
	"""Ktwo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ktwo", core, parent)

	def set(self, cell_name: str, k_2: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MSG<id>:TDOMain:KTWO \n
		Snippet: driver.configure.signaling.nradio.cell.msg.tdomain.ktwo.set(cell_name = 'abc', k_2 = 1) \n
		Configures k2 influencing the slot offset between msg2 and msg3. \n
			:param cell_name: No help available
			:param k_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('k_2', k_2, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:MSG3:TDOMain:KTWO {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MSG<id>:TDOMain:KTWO \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.msg.tdomain.ktwo.get(cell_name = 'abc') \n
		Configures k2 influencing the slot offset between msg2 and msg3. \n
			:param cell_name: No help available
			:return: k_2: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:MSG3:TDOMain:KTWO? {param}')
		return Conversions.str_to_int(response)
