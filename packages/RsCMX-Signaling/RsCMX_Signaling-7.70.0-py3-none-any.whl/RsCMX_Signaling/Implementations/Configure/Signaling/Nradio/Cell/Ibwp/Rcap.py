from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcapCls:
	"""Rcap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcap", core, parent)

	def set(self, cell_name: str, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:RCAP \n
		Snippet: driver.configure.signaling.nradio.cell.ibwp.rcap.set(cell_name = 'abc', enable = False) \n
		Selects whether the initial BWP is specific for RedCap or not. \n
			:param cell_name: No help available
			:param enable:
				- ON: The initial BWP is specific for RedCap. It is signaled via 'initialUplinkBWP-RedCap-r17' and 'initialDownlinkBWP-RedCap-r17'.
				- OFF: The initial BWP is not specific for RedCap. It is signaled via 'initialUplinkBWP' and 'initialDownlinkBWP'."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:RCAP {param}'.rstrip())

	def get(self, cell_name: str) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:RCAP \n
		Snippet: value: bool = driver.configure.signaling.nradio.cell.ibwp.rcap.get(cell_name = 'abc') \n
		Selects whether the initial BWP is specific for RedCap or not. \n
			:param cell_name: No help available
			:return: enable:
				- ON: The initial BWP is specific for RedCap. It is signaled via 'initialUplinkBWP-RedCap-r17' and 'initialDownlinkBWP-RedCap-r17'.
				- OFF: The initial BWP is not specific for RedCap. It is signaled via 'initialUplinkBWP' and 'initialDownlinkBWP'."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:RCAP? {param}')
		return Conversions.str_to_bool(response)
