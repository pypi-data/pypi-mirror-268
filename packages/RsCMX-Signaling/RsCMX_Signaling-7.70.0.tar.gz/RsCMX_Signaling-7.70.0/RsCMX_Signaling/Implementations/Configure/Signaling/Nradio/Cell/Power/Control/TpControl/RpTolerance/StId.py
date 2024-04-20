from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StIdCls:
	"""StId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stId", core, parent)

	def set(self, cell_name: str, sub_test_id: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:STID \n
		Snippet: driver.configure.signaling.nradio.cell.power.control.tpControl.rpTolerance.stId.set(cell_name = 'abc', sub_test_id = 1) \n
		Selects the subtest ID for relative power tolerance tests, for the initial BWP. \n
			:param cell_name: No help available
			:param sub_test_id: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('sub_test_id', sub_test_id, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:STID {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:STID \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.power.control.tpControl.rpTolerance.stId.get(cell_name = 'abc') \n
		Selects the subtest ID for relative power tolerance tests, for the initial BWP. \n
			:param cell_name: No help available
			:return: sub_test_id: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:STID? {param}')
		return Conversions.str_to_int(response)
