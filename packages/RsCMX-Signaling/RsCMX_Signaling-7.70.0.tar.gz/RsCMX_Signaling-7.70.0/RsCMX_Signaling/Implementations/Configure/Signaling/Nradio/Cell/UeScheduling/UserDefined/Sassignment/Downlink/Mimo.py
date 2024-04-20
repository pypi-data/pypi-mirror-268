from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	def set(self, cell_name: str, slot: int, mimo: enums.Mimo) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:MIMO \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.mimo.set(cell_name = 'abc', slot = 1, mimo = enums.Mimo.M22) \n
		Specifies the MIMO scheme for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:param mimo: SISO: 1xN M22: 2xN M33: 3xN M44: 4xN
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer), ArgSingle('mimo', mimo, DataType.Enum, enums.Mimo))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:MIMO {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, slot: int) -> enums.Mimo:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:MIMO \n
		Snippet: value: enums.Mimo = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.sassignment.downlink.mimo.get(cell_name = 'abc', slot = 1) \n
		Specifies the MIMO scheme for the DL slot with the index <Slot>, for the initial BWP. \n
			:param cell_name: No help available
			:param slot: No help available
			:return: mimo: SISO: 1xN M22: 2xN M33: 3xN M44: 4xN"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:SASSignment:DL:MIMO? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.Mimo)
