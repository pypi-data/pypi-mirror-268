from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set_execute(self, cell_name: str) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:PATTern:EXECute \n
		Snippet: driver.procedure.signaling.nradio.cell.power.control.tpControl.pattern.set_execute(cell_name = 'abc') \n
		Starts the execution of a user-defined TPC pattern, for the initial BWP. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:PATTern:EXECute {param}')
