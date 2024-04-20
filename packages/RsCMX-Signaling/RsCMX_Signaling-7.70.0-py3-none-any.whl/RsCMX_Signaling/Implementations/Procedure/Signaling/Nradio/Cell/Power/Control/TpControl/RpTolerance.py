from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpToleranceCls:
	"""RpTolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpTolerance", core, parent)

	def set_execute(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:EXECute \n
		Snippet: driver.procedure.signaling.nradio.cell.power.control.tpControl.rpTolerance.set_execute(cell_name = 'abc') \n
		Starts the execution of the TPC pattern for relative power tolerance tests, for the initial BWP. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance:EXECute {param}')
