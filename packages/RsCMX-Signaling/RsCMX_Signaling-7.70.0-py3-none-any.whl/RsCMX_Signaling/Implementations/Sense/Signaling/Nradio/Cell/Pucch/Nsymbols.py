from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NsymbolsCls:
	"""Nsymbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsymbols", core, parent)

	def get(self, cell_name: str) -> int:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:PUCCh:NSYMbols \n
		Snippet: value: int = driver.sense.signaling.nradio.cell.pucch.nsymbols.get(cell_name = 'abc') \n
		Queries the number of allocated OFDM symbols resulting from the PUCCH format, for the initial BWP. \n
			:param cell_name: No help available
			:return: no_symbols: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:PUCCh:NSYMbols? {param}')
		return Conversions.str_to_int(response)
