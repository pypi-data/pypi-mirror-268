from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DbwpCls:
	"""Dbwp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbwp", core, parent)

	def set(self, cell_name: str, bwp: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CA:SCELl:DORMancy:DBWP \n
		Snippet: driver.configure.signaling.nradio.ca.scell.dormancy.dbwp.set(cell_name = 'abc', bwp = 1) \n
		Selects the target DL BWP for switching the cell state to dormant ('dormantBWP-Id') . \n
			:param cell_name: No help available
			:param bwp: IBWP: initial BWP integer: BWP ID
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('bwp', bwp, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CA:SCELl:DORMancy:DBWP {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CA:SCELl:DORMancy:DBWP \n
		Snippet: value: int = driver.configure.signaling.nradio.ca.scell.dormancy.dbwp.get(cell_name = 'abc') \n
		Selects the target DL BWP for switching the cell state to dormant ('dormantBWP-Id') . \n
			:param cell_name: No help available
			:return: bwp: IBWP: initial BWP integer: BWP ID"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CA:SCELl:DORMancy:DBWP? {param}')
		return Conversions.str_to_int(response)
