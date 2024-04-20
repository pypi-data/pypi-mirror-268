from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChmappingCls:
	"""Chmapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chmapping", core, parent)

	def set(self, cell_name: str, slot: int, mapping: enums.Mapping) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:CHMapping \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.tdomain.chmapping.set(cell_name = 'abc', slot = 1, mapping = enums.Mapping.A) \n
		Selects the type of PDSCH mapping, for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:param mapping: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer), ArgSingle('mapping', mapping, DataType.Enum, enums.Mapping))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:CHMapping {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, slot: int) -> enums.Mapping:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:CHMapping \n
		Snippet: value: enums.Mapping = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.tdomain.chmapping.get(cell_name = 'abc', slot = 1) \n
		Selects the type of PDSCH mapping, for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: mapping: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:TDOMain:CHMapping? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.Mapping)
