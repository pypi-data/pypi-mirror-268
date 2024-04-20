from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MacCls:
	"""Mac commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mac", core, parent)

	def set(self, cell_name: str, activation: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CA:SCELl:MAC \n
		Snippet: driver.configure.signaling.nradio.ca.scell.mac.set(cell_name = 'abc', activation = False) \n
		Enables or disables the retransmission of the MAC activation CE message for SCells if the activation is not acknowledged
		by the UE. Modifying this setting for a cell modifies it also for all other cells of the cell group. \n
			:param cell_name: No help available
			:param activation: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('activation', activation, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CA:SCELl:MAC {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CA:SCELl:MAC \n
		Snippet: value: bool = driver.configure.signaling.nradio.ca.scell.mac.get(cell_name = 'abc') \n
		Enables or disables the retransmission of the MAC activation CE message for SCells if the activation is not acknowledged
		by the UE. Modifying this setting for a cell modifies it also for all other cells of the cell group. \n
			:param cell_name: No help available
			:return: activation: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CA:SCELl:MAC? {param}')
		return Conversions.str_to_bool(response)
