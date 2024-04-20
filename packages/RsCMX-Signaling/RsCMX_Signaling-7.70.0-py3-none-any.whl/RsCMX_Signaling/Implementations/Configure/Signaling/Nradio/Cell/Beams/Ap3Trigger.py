from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ap3TriggerCls:
	"""Ap3Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ap3Trigger", core, parent)

	def set(self, cell_name: str, auto_p_3_trigger: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAMs:AP3Trigger \n
		Snippet: driver.configure.signaling.nradio.cell.beams.ap3Trigger.set(cell_name = 'abc', auto_p_3_trigger = False) \n
		Configures automatic triggering of the P-3 process upon update of the active CSI-RS beam. \n
			:param cell_name: No help available
			:param auto_p_3_trigger: Automatic triggering OFF or ON.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('auto_p_3_trigger', auto_p_3_trigger, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAMs:AP3Trigger {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAMs:AP3Trigger \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.beams.ap3Trigger.get(cell_name = 'abc') \n
		Configures automatic triggering of the P-3 process upon update of the active CSI-RS beam. \n
			:param cell_name: No help available
			:return: auto_p_3_trigger: Automatic triggering OFF or ON."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BEAMs:AP3Trigger? {param}')
		return Conversions.str_to_bool(response)
