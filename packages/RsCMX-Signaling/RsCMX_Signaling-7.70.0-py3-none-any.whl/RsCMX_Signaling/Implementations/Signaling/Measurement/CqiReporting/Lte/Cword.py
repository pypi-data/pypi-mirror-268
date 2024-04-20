from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CwordCls:
	"""Cword commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Cword, default value after init: Cword.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cword", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cword_get', 'repcap_cword_set', repcap.Cword.Nr1)

	def repcap_cword_set(self, cword: repcap.Cword) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Cword.Default
		Default value after init: Cword.Nr1"""
		self._cmd_group.set_repcap_enum_value(cword)

	def repcap_cword_get(self) -> repcap.Cword:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability indicator'
			- Cell_Name: List[str]: Name of the cell for which the values are reported.
			- Median_Cqi: List[int]: Median of the CQI values reported by the UE.
			- Range_Median_Rel: List[float]: Number of received CQI values in the range (median CQI - 1) to (median CQI + 1) , as percentage of TotalNoReports.
			- Range_Median_Abs: List[int]: Number of received CQI values in the range (median CQI - 1) to (median CQI + 1) , as absolute value.
			- Total_No_Reports: List[int]: Total number of received CQI values."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Cell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Median_Cqi', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Range_Median_Rel', DataType.FloatList, None, False, True, 1),
			ArgStruct('Range_Median_Abs', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Total_No_Reports', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Cell_Name: List[str] = None
			self.Median_Cqi: List[int] = None
			self.Range_Median_Rel: List[float] = None
			self.Range_Median_Abs: List[int] = None
			self.Total_No_Reports: List[int] = None

	def fetch(self, cword=repcap.Cword.Default) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:MEASurement:CQIReporting:LTE:CWORd<no> \n
		Snippet: value: FetchStruct = driver.signaling.measurement.cqiReporting.lte.cword.fetch(cword = repcap.Cword.Default) \n
		Returns the statistical evaluation of the histogram of reported CQI values. There are separate commands for LTE cells and
		NR cells. And there is one set of results {...} per cell: <Reliability>, {<CellName>, <MedianCqi>, <RangeMedianRel>,
		<RangeMedianAbs>, <TotalNoReports>}, {...}, ... \n
			:param cword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cword')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		cword_cmd_val = self._cmd_group.get_repcap_cmd_value(cword, repcap.Cword)
		return self._core.io.query_struct(f'FETCh:SIGNaling:MEASurement:CQIReporting:LTE:CWORd{cword_cmd_val}?', self.__class__.FetchStruct())

	def clone(self) -> 'CwordCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CwordCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
