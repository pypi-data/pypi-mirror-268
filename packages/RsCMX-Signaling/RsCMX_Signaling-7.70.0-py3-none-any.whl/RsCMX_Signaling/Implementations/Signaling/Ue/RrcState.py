from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrcStateCls:
	"""RrcState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrcState", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Rrc_State: enums.RrcState: No parameter help available
			- Uec_State: enums.UecState: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rrc_State', enums.RrcState),
			ArgStruct.scalar_enum('Uec_State', enums.UecState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rrc_State: enums.RrcState = None
			self.Uec_State: enums.UecState = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:UE:RRCState \n
		Snippet: value: FetchStruct = driver.signaling.ue.rrcState.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:SIGNaling:UE:RRCState?', self.__class__.FetchStruct())
