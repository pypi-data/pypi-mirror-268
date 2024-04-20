from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DltShiftCls:
	"""DltShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dltShift", core, parent)

	def set(self, cell_name: str, delta: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TIMing:DLTShift \n
		Snippet: driver.configure.signaling.lte.cell.timing.dltShift.set(cell_name = 'abc', delta = 1) \n
		Adds an offset to the DL timing, relative to the current timing. The setting is only configurable during a connection.
		Each time you change the setting, the new value is added to the previous timing. So the values accumulate.
		A query returns the last setting and the total accumulated value: <Delta>, <Total>. \n
			:param cell_name: No help available
			:param delta: Offset in Ts
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('delta', delta, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:TIMing:DLTShift {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Delta: int: Offset in Ts
			- Total: int: Total accumulated offsets"""
		__meta_args_list = [
			ArgStruct.scalar_int('Delta'),
			ArgStruct.scalar_int('Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Delta: int = None
			self.Total: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:TIMing:DLTShift \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.timing.dltShift.get(cell_name = 'abc') \n
		Adds an offset to the DL timing, relative to the current timing. The setting is only configurable during a connection.
		Each time you change the setting, the new value is added to the previous timing. So the values accumulate.
		A query returns the last setting and the total accumulated value: <Delta>, <Total>. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:TIMing:DLTShift? {param}', self.__class__.GetStruct())
