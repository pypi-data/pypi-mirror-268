from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SerialCls:
	"""Serial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("serial", core, parent)

	def set(self, network_scope: str, display_mode: enums.DisplayMode, message_code: int = None, update_time: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:SERial \n
		Snippet: driver.configure.signaling.cmas.serial.set(network_scope = 'abc', display_mode = enums.DisplayMode.IMMediate, message_code = 1, update_time = 1) \n
		Defines settings influencing the serial number for CMAS messages. \n
			:param network_scope: No help available
			:param display_mode: IMMediate: The UE displays a message immediately. NORMal: The UE displays a message upon user action.
			:param message_code: The last 8 bits of the message code of the serial number.
			:param update_time: The version of the message transmitted as an update number.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('network_scope', network_scope, DataType.String), ArgSingle('display_mode', display_mode, DataType.Enum, enums.DisplayMode), ArgSingle('message_code', message_code, DataType.Integer, None, is_optional=True), ArgSingle('update_time', update_time, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:CMAS:SERial {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Display_Mode: enums.DisplayMode: IMMediate: The UE displays a message immediately. NORMal: The UE displays a message upon user action.
			- Message_Code: int: The last 8 bits of the message code of the serial number.
			- Update_Time: int: The version of the message transmitted as an update number."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Display_Mode', enums.DisplayMode),
			ArgStruct.scalar_int('Message_Code'),
			ArgStruct.scalar_int('Update_Time')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Display_Mode: enums.DisplayMode = None
			self.Message_Code: int = None
			self.Update_Time: int = None

	def get(self, network_scope: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:CMAS:SERial \n
		Snippet: value: GetStruct = driver.configure.signaling.cmas.serial.get(network_scope = 'abc') \n
		Defines settings influencing the serial number for CMAS messages. \n
			:param network_scope: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(network_scope)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:CMAS:SERial? {param}', self.__class__.GetStruct())
