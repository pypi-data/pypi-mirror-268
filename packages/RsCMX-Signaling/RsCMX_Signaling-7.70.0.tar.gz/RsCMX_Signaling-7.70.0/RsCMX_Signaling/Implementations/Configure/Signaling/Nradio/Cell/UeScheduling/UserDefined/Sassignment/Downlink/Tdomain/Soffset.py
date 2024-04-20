from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SoffsetCls:
	"""Soffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soffset", core, parent)

	def set(self, cell_name: str, slot: int, offset: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:SOFFset \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.tdomain.soffset.set(cell_name = 'abc', slot = 1, offset = 1) \n
		Configures the slot offset k0 for the PDSCH, for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:param offset: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer), ArgSingle('offset', offset, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:SOFFset {param}'.rstrip())

	def get(self, cell_name: str, slot: int) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:SOFFset \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.tdomain.soffset.get(cell_name = 'abc', slot = 1) \n
		Configures the slot offset k0 for the PDSCH, for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: offset: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:SOFFset? {param}'.rstrip())
		return Conversions.str_to_int(response)
