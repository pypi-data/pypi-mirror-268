from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaprCls:
	"""Papr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("papr", core, parent)

	def set(self, cell_name: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:MTA:PAPR \n
		Snippet: driver.configure.signaling.nradio.cell.dmrs.uplink.mta.papr.set(cell_name = 'abc', enable = False) \n
		Enables the usage of a DMRS with a low PAPR, for PUSCH, mapping type A, initial BWP. \n
			:param cell_name: No help available
			:param enable: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:MTA:PAPR {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:DMRS:UL:MTA:PAPR \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.dmrs.uplink.mta.papr.get(cell_name = 'abc') \n
		Enables the usage of a DMRS with a low PAPR, for PUSCH, mapping type A, initial BWP. \n
			:param cell_name: No help available
			:return: enable: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:DMRS:UL:MTA:PAPR? {param}')
		return Conversions.str_to_bool(response)
