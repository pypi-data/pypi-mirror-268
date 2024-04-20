from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlockCls:
	"""Block commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("block", core, parent)

	def set(self, cell_name: str, mode: enums.Mode, index: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FOLLowing:BLOCk \n
		Snippet: driver.configure.signaling.nradio.cell.beam.following.block.set(cell_name = 'abc', mode = enums.Mode.BINDex, index = 1) \n
		Selects a beamlock target. \n
			:param cell_name: No help available
			:param mode: Type of value to be used for target selection. SSBBeam: SSB beam index BINDex: beam index CSIRs: NZP CSI-RS resource ID
			:param index: Value of the type Mode, e.g. an SBB beam index value.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.Mode), ArgSingle('index', index, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FOLLowing:BLOCk {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Mode: enums.Mode: Type of value to be used for target selection. SSBBeam: SSB beam index BINDex: beam index CSIRs: NZP CSI-RS resource ID
			- Index: int: Value of the type Mode, e.g. an SBB beam index value."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mode', enums.Mode),
			ArgStruct.scalar_int('Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mode: enums.Mode = None
			self.Index: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FOLLowing:BLOCk \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.beam.following.block.get(cell_name = 'abc') \n
		Selects a beamlock target. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FOLLowing:BLOCk? {param}', self.__class__.GetStruct())
