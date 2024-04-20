from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsidCls:
	"""Ssid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssid", core, parent)

	def set(self, cell_name: str, idn: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:SSID \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.ssid.set(cell_name = 'abc', idn = 1) \n
		Configures the ID of the search space for the UL, for the initial BWP. \n
			:param cell_name: No help available
			:param idn: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('idn', idn, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:SSID {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:SSID \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.ssid.get(cell_name = 'abc') \n
		Configures the ID of the search space for the UL, for the initial BWP. \n
			:param cell_name: No help available
			:return: idn: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:SSID? {param}')
		return Conversions.str_to_int(response)
