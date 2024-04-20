from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcpCls:
	"""Pdcp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcp", core, parent)

	def set(self, enable: bool, log_type: enums.LogType, payload: int = None) -> None:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP \n
		Snippet: driver.diagnostic.signaling.lte.cell.logging.pdcp.set(enable = False, log_type = enums.LogType.DISable, payload = 1) \n
		No command help available \n
			:param enable: No help available
			:param log_type: No help available
			:param payload: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('log_type', log_type, DataType.Enum, enums.LogType), ArgSingle('payload', payload, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP {param}'.rstrip())

	# noinspection PyTypeChecker
	class PdcpStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- Log_Type: enums.LogType: No parameter help available
			- Payload: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Log_Type', enums.LogType),
			ArgStruct.scalar_int('Payload')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Log_Type: enums.LogType = None
			self.Payload: int = None

	def get(self) -> PdcpStruct:
		"""SCPI: DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP \n
		Snippet: value: PdcpStruct = driver.diagnostic.signaling.lte.cell.logging.pdcp.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PdcpStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:SIGNaling:LTE:CELL:LOGGing:PDCP?', self.__class__.PdcpStruct())
