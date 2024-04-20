from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrcRejectCls:
	"""RrcReject commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrcReject", core, parent)

	def set(self, reject_procedure: enums.FgsRejectProcedure, reject_cause: enums.FgsRejectCause = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NBEHavior:RRCReject \n
		Snippet: driver.configure.signaling.fgs.nbehavior.rrcReject.set(reject_procedure = enums.FgsRejectProcedure.AUTR, reject_cause = enums.FgsRejectCause.C003) \n
		Configures RRC reject causes for 5GS tracking areas. \n
			:param reject_procedure: Selects the procedure to fail. NOR: No reject. REGR: 'Register Reject' message AUTR: 'Authentication Reject' message PDUR: 'PDU Session Establishment Reject' message
			:param reject_cause: Selects the cause to be signaled to the UE as the reason for the rejection.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('reject_procedure', reject_procedure, DataType.Enum, enums.FgsRejectProcedure), ArgSingle('reject_cause', reject_cause, DataType.Enum, enums.FgsRejectCause, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NBEHavior:RRCReject {param}'.rstrip())

	# noinspection PyTypeChecker
	class RrcRejectStruct(StructBase):
		"""Response structure. Fields: \n
			- Reject_Procedure: enums.FgsRejectProcedure: Selects the procedure to fail. NOR: No reject. REGR: 'Register Reject' message AUTR: 'Authentication Reject' message PDUR: 'PDU Session Establishment Reject' message
			- Reject_Cause: enums.FgsRejectCause: Selects the cause to be signaled to the UE as the reason for the rejection."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Reject_Procedure', enums.FgsRejectProcedure),
			ArgStruct.scalar_enum('Reject_Cause', enums.FgsRejectCause)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reject_Procedure: enums.FgsRejectProcedure = None
			self.Reject_Cause: enums.FgsRejectCause = None

	def get(self) -> RrcRejectStruct:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NBEHavior:RRCReject \n
		Snippet: value: RrcRejectStruct = driver.configure.signaling.fgs.nbehavior.rrcReject.get() \n
		Configures RRC reject causes for 5GS tracking areas. \n
			:return: structure: for return value, see the help for RrcRejectStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:SIGNaling:FGS:NBEHavior:RRCReject?', self.__class__.RrcRejectStruct())
