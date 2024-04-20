from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmatrixCls:
	"""Cmatrix commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmatrix", core, parent)

	def set_hadamard(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:CMATrix:HADamard \n
		Snippet: driver.procedure.signaling.nradio.cell.cmatrix.set_hadamard(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:CMATrix:HADamard {param}')

	def set_tgpp(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:CMATrix:TGPP \n
		Snippet: driver.procedure.signaling.nradio.cell.cmatrix.set_tgpp(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:CMATrix:TGPP {param}')
