from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BearerCls:
	"""Bearer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bearer", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Linked_Bearer_Id: List[int]: ID of the linked default bearer
			- Bearer_Id: List[int]: ID of the dedicated bearer"""
		__meta_args_list = [
			ArgStruct('Linked_Bearer_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Bearer_Id', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Linked_Bearer_Id: List[int] = None
			self.Bearer_Id: List[int] = None

	def get(self, ue_id: str = None) -> GetStruct:
		"""SCPI: CATalog:SIGNaling:LTE:UE:BEARer \n
		Snippet: value: GetStruct = driver.catalog.signaling.lte.ue.bearer.get(ue_id = 'abc') \n
		Queries a list of all established dedicated bearers. For each dedicated bearer, two IDs are returned: {<LinkedBearerId>,
		<BearerId>}bearer 1, {<LinkedBearerId>, <BearerId>}bearer 2, ... \n
			:param ue_id: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True))
		return self._core.io.query_struct(f'CATalog:SIGNaling:LTE:UE:BEARer? {param}'.rstrip(), self.__class__.GetStruct())
