from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EarfcnCls:
	"""Earfcn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("earfcn", core, parent)

	def set(self, cell_name: str, channel: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:EARFcn \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.uplink.earfcn.set(cell_name = 'abc', channel = 1) \n
		Selects the UL channel number. The DL channel number is not changed. \n
			:param cell_name: No help available
			:param channel: HASYmmetric refers to the high DL-only range, e.g. for band 66.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('channel', channel, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:EARFcn {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:UL:EARFcn \n
		Snippet: value: int = driver.configure.signaling.lte.cell.rfSettings.uplink.earfcn.get(cell_name = 'abc') \n
		Selects the UL channel number. The DL channel number is not changed. \n
			:param cell_name: No help available
			:return: channel: HASYmmetric refers to the high DL-only range, e.g. for band 66."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:UL:EARFcn? {param}')
		return Conversions.str_to_int(response)
