from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImsiCls:
	"""Imsi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imsi", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Identity_Type: enums.IdentityType: IMSI: international mobile subscriber identity NAI: network specific identifier (NSI) GCI: global cable identifier GLI: global line identifier
			- Identity: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Identity_Type', enums.IdentityType),
			ArgStruct.scalar_str('Identity')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Identity_Type: enums.IdentityType = None
			self.Identity: str = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:UE:IMSI \n
		Snippet: value: FetchStruct = driver.signaling.ue.imsi.fetch() \n
		Queries the identity reported by the UE. In an EPS tracking area, the UE sends an IMSI. In a 5GS tracking area, it can
		also send an NSI, GCI or GLI. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:UE:IMSI?', self.__class__.FetchStruct())
