from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeTypeCls:
	"""UeType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueType", core, parent)

	def set(self, cell_name: str, ue_type: enums.UeType) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UETYpe \n
		Snippet: driver.configure.signaling.nradio.cell.ueType.set(cell_name = 'abc', ue_type = enums.UeType.NORMal) \n
		Select the type of your UE (normal UE or RedCap UE) in edit mode. \n
			:param cell_name: No help available
			:param ue_type: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ue_type', ue_type, DataType.Enum, enums.UeType))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UETYpe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.UeType:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UETYpe \n
		Snippet: value: enums.UeType = driver.configure.signaling.nradio.cell.ueType.get(cell_name = 'abc') \n
		Select the type of your UE (normal UE or RedCap UE) in edit mode. \n
			:param cell_name: No help available
			:return: ue_type: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UETYpe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.UeType)
