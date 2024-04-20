from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpToleranceCls:
	"""RpTolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpTolerance", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Start_Power: float: Initial power level to which the UE is commanded before executing the actual TPC pattern.
			- Length: int: Number of active UL slots in the TPC pattern (after the start power) .
			- Rb_Change_Pos: int: Position of the RB allocation change within the TPC pattern (number of UL subframes) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Start_Power'),
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Rb_Change_Pos')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Power: float = None
			self.Length: int = None
			self.Rb_Change_Pos: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance \n
		Snippet: value: GetStruct = driver.sense.signaling.nradio.cell.power.control.tpControl.rpTolerance.get(cell_name = 'abc') \n
		Queries information about the TPC pattern configured for relative power tolerance tests for the initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'SENSe:SIGNaling:NRADio:CELL:POWer:CONTrol:TPControl:RPTolerance? {param}', self.__class__.GetStruct())
