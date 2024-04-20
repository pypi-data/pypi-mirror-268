from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcidCls:
	"""Pcid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcid", core, parent)

	def set(self, cell_name: str, idn: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:PCID \n
		Snippet: driver.configure.signaling.lte.cell.pcid.set(cell_name = 'abc', idn = 1) \n
		Defines the physical cell ID. \n
			:param cell_name: No help available
			:param idn: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('idn', idn, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:PCID {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:PCID \n
		Snippet: value: int = driver.configure.signaling.lte.cell.pcid.get(cell_name = 'abc') \n
		Defines the physical cell ID. \n
			:param cell_name: No help available
			:return: idn: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:PCID? {param}')
		return Conversions.str_to_int(response)
