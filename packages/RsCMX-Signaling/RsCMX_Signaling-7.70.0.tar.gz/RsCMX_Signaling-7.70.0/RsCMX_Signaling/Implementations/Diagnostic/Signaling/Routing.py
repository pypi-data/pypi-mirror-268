from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RoutingCls:
	"""Routing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("routing", core, parent)

	def set(self, routing: enums.Routing, cell_signal: enums.DiagCellSignal = None, baseband: enums.DiagBaseband = None, tdd: enums.Tdd = None) -> None:
		"""SCPI: DIAGnostic:SIGNaling:ROUTing \n
		Snippet: driver.diagnostic.signaling.routing.set(routing = enums.Routing.DUT, cell_signal = enums.DiagCellSignal.COMBining, baseband = enums.DiagBaseband.BBCombining, tdd = enums.Tdd.CP1) \n
		No command help available \n
			:param routing: No help available
			:param cell_signal: No help available
			:param baseband: No help available
			:param tdd: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('routing', routing, DataType.Enum, enums.Routing), ArgSingle('cell_signal', cell_signal, DataType.Enum, enums.DiagCellSignal, is_optional=True), ArgSingle('baseband', baseband, DataType.Enum, enums.DiagBaseband, is_optional=True), ArgSingle('tdd', tdd, DataType.Enum, enums.Tdd, is_optional=True))
		self._core.io.write(f'DIAGnostic:SIGNaling:ROUTing {param}'.rstrip())

	# noinspection PyTypeChecker
	class RoutingStruct(StructBase):
		"""Response structure. Fields: \n
			- Routing: enums.Routing: No parameter help available
			- Cell_Signal: enums.DiagCellSignal: No parameter help available
			- Baseband: enums.DiagBaseband: No parameter help available
			- Tdd: enums.Tdd: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Routing', enums.Routing),
			ArgStruct.scalar_enum('Cell_Signal', enums.DiagCellSignal),
			ArgStruct.scalar_enum('Baseband', enums.DiagBaseband),
			ArgStruct.scalar_enum('Tdd', enums.Tdd)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Routing: enums.Routing = None
			self.Cell_Signal: enums.DiagCellSignal = None
			self.Baseband: enums.DiagBaseband = None
			self.Tdd: enums.Tdd = None

	def get(self) -> RoutingStruct:
		"""SCPI: DIAGnostic:SIGNaling:ROUTing \n
		Snippet: value: RoutingStruct = driver.diagnostic.signaling.routing.get() \n
		No command help available \n
			:return: structure: for return value, see the help for RoutingStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:SIGNaling:ROUTing?', self.__class__.RoutingStruct())
