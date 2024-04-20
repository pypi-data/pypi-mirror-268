from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- State: enums.State: OFF: Measurement off, no results. RDY: Measurement finished, valid results can be available. RUN: Measurement running.
			- Cell_Name: str: No parameter help available
			- Cell_Type: enums.CellType: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('State', enums.State),
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Cell_Type', enums.CellType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: enums.State = None
			self.Cell_Name: str = None
			self.Cell_Type: enums.CellType = None

	def fetch(self, info: enums.Info = None) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:BLER:STATe \n
		Snippet: value: FetchStruct = driver.signaling.measurement.bler.state.fetch(info = enums.Info.ALL) \n
		Queries the measurement state. \n
			:param info: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('info', info, DataType.Enum, enums.Info, is_optional=True))
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:BLER:STATe? {param}'.rstrip(), self.__class__.FetchStruct())
