from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TmodeCls:
	"""Tmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmode", core, parent)

	# noinspection PyTypeChecker
	class SsReportStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Measured_Ssb_Id: float: ID of the SSB for which the RSRP values are reported.
			- Branch_0: float: RSRP value reported by the UE for its receiver branch 0.
			- Branch_1: float: RSRP value reported by the UE for its receiver branch 1."""
		__meta_args_list = [
			ArgStruct.scalar_float('Measured_Ssb_Id'),
			ArgStruct.scalar_float('Branch_0'),
			ArgStruct.scalar_float('Branch_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Measured_Ssb_Id: float = None
			self.Branch_0: float = None
			self.Branch_1: float = None

	def get_ss_report(self) -> SsReportStruct:
		"""SCPI: SENSe:SIGNaling:TMODe:SSReport \n
		Snippet: value: SsReportStruct = driver.sense.signaling.tmode.get_ss_report() \n
		Queries SS-RSRPB report contents received from the UE. \n
			:return: structure: for return value, see the help for SsReportStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:SIGNaling:TMODe:SSReport?', self.__class__.SsReportStruct())
