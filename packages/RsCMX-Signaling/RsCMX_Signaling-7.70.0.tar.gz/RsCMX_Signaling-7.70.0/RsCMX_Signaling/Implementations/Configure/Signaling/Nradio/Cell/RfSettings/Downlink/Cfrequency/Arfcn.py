from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ArfcnCls:
	"""Arfcn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arfcn", core, parent)

	def set(self, cell_name: str, number: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:DL:CFRequency:ARFCn \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.downlink.cfrequency.arfcn.set(cell_name = 'abc', number = 1) \n
		Configures the ARFCN for the DL carrier center frequency \n
			:param cell_name: No help available
			:param number: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('number', number, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:DL:CFRequency:ARFCn {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:DL:CFRequency:ARFCn \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.rfSettings.downlink.cfrequency.arfcn.get(cell_name = 'abc') \n
		Configures the ARFCN for the DL carrier center frequency \n
			:param cell_name: No help available
			:return: number: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:DL:CFRequency:ARFCn? {param}')
		return Conversions.str_to_int(response)
