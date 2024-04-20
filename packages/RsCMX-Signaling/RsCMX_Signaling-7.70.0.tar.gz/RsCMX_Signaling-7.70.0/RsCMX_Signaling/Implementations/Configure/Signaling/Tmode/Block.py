from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlockCls:
	"""Block commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("block", core, parent)

	def set(self, enable: bool, test_function: enums.TestFunction = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:BLOCk \n
		Snippet: driver.configure.signaling.tmode.block.set(enable = False, test_function = enums.TestFunction.RX) \n
		Enables or disables the beamlock function of the UE and selects the direction for enabled beamlock. \n
			:param enable: Enable / disable the beamlock function.
			:param test_function: RX: Beamlock for UE receiver beams. TX: Beamlock for UE transmitter beams. RXTX: Beamlock for UE receiver and transmitter beams.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('test_function', test_function, DataType.Enum, enums.TestFunction, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:TMODe:BLOCk {param}'.rstrip())

	# noinspection PyTypeChecker
	class BlockStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enable / disable the beamlock function.
			- Test_Function: enums.TestFunction: RX: Beamlock for UE receiver beams. TX: Beamlock for UE transmitter beams. RXTX: Beamlock for UE receiver and transmitter beams."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Test_Function', enums.TestFunction)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Test_Function: enums.TestFunction = None

	def get(self) -> BlockStruct:
		"""SCPI: [CONFigure]:SIGNaling:TMODe:BLOCk \n
		Snippet: value: BlockStruct = driver.configure.signaling.tmode.block.get() \n
		Enables or disables the beamlock function of the UE and selects the direction for enabled beamlock. \n
			:return: structure: for return value, see the help for BlockStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TMODe:BLOCk?', self.__class__.BlockStruct())
