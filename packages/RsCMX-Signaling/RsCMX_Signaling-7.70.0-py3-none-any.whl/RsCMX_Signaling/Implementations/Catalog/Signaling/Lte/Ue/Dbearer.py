from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DbearerCls:
	"""Dbearer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbearer", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Linked_Bearer_Id: List[int]: ID of the default bearer
			- Apn: List[str]: APN of the default bearer"""
		__meta_args_list = [
			ArgStruct('Linked_Bearer_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Apn', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Linked_Bearer_Id: List[int] = None
			self.Apn: List[str] = None

	def get(self, ue_id: str = None) -> GetStruct:
		"""SCPI: CATalog:SIGNaling:LTE:UE:DBEarer \n
		Snippet: value: GetStruct = driver.catalog.signaling.lte.ue.dbearer.get(ue_id = 'abc') \n
		Queries a list of all established default bearers. For each default bearer, two values are returned: {<BearerId>,
		<APN>}bearer 1, {<BearerId>, <APN>}bearer 2, ... \n
			:param ue_id: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True))
		return self._core.io.query_struct(f'CATalog:SIGNaling:LTE:UE:DBEarer? {param}'.rstrip(), self.__class__.GetStruct())
