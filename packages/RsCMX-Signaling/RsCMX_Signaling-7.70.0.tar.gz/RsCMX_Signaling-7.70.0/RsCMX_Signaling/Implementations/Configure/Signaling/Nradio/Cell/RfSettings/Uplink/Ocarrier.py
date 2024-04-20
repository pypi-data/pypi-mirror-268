from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OcarrierCls:
	"""Ocarrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ocarrier", core, parent)

	def set(self, cell_name: str, offset_to_carrier: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:UL:OCARrier \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.uplink.ocarrier.set(cell_name = 'abc', offset_to_carrier = 1) \n
		Defines the offset to carrier for the uplink. \n
			:param cell_name: No help available
			:param offset_to_carrier: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('offset_to_carrier', offset_to_carrier, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:UL:OCARrier {param}'.rstrip())

	def get(self, cell_name: str) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:UL:OCARrier \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.rfSettings.uplink.ocarrier.get(cell_name = 'abc') \n
		Defines the offset to carrier for the uplink. \n
			:param cell_name: No help available
			:return: offset_to_carrier: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:UL:OCARrier? {param}')
		return Conversions.str_to_int(response)
