from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BearerCls:
	"""Bearer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bearer", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Ue_Id: str: No parameter help available
			- Bearer_Id: int: No parameter help available
			- Qci: enums.Qi: Optional setting parameter. Value of the quality of service class identifier. Values defined in 3GPP TS 23.203, table 6.1.7. The GUI shows the designation of each value.
			- Max_Dl_Bitrate: int: Optional setting parameter. Maximum DL bit rate allowed in the network.
			- Max_Ul_Bitrate: int: Optional setting parameter. Maximum UL bit rate allowed in the network.
			- Gtd_Dl_Bitrate: int: Optional setting parameter. DL bit rate guaranteed by the network for the bearer.
			- Gtd_Ul_Bitrate: int: Optional setting parameter. UL bit rate guaranteed by the network for the bearer."""
		__meta_args_list = [
			ArgStruct.scalar_str('Ue_Id'),
			ArgStruct.scalar_int('Bearer_Id'),
			ArgStruct.scalar_enum_optional('Qci', enums.Qi),
			ArgStruct.scalar_int_optional('Max_Dl_Bitrate'),
			ArgStruct.scalar_int_optional('Max_Ul_Bitrate'),
			ArgStruct.scalar_int_optional('Gtd_Dl_Bitrate'),
			ArgStruct.scalar_int_optional('Gtd_Ul_Bitrate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Id: str = None
			self.Bearer_Id: int = None
			self.Qci: enums.Qi = None
			self.Max_Dl_Bitrate: int = None
			self.Max_Ul_Bitrate: int = None
			self.Gtd_Dl_Bitrate: int = None
			self.Gtd_Ul_Bitrate: int = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:BEARer \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.ue.bearer.SetStruct() \n
		structure.Ue_Id: str = 'abc' \n
		structure.Bearer_Id: int = 1 \n
		structure.Qci: enums.Qi = enums.Qi.Q1 \n
		structure.Max_Dl_Bitrate: int = 1 \n
		structure.Max_Ul_Bitrate: int = 1 \n
		structure.Gtd_Dl_Bitrate: int = 1 \n
		structure.Gtd_Ul_Bitrate: int = 1 \n
		driver.configure.signaling.lte.ue.bearer.set(structure) \n
		Configures the existing bearer with the <BearerId>. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:UE:BEARer', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Qci: enums.Qi: Value of the quality of service class identifier. Values defined in 3GPP TS 23.203, table 6.1.7. The GUI shows the designation of each value.
			- Max_Dl_Bitrate: int: Maximum DL bit rate allowed in the network.
			- Max_Ul_Bitrate: int: Maximum UL bit rate allowed in the network.
			- Gtd_Dl_Bitrate: int: DL bit rate guaranteed by the network for the bearer.
			- Gtd_Ul_Bitrate: int: UL bit rate guaranteed by the network for the bearer."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Qci', enums.Qi),
			ArgStruct.scalar_int('Max_Dl_Bitrate'),
			ArgStruct.scalar_int('Max_Ul_Bitrate'),
			ArgStruct.scalar_int('Gtd_Dl_Bitrate'),
			ArgStruct.scalar_int('Gtd_Ul_Bitrate')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Qci: enums.Qi = None
			self.Max_Dl_Bitrate: int = None
			self.Max_Ul_Bitrate: int = None
			self.Gtd_Dl_Bitrate: int = None
			self.Gtd_Ul_Bitrate: int = None

	def get(self, ue_id: str, bearer_id: int) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:BEARer \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.ue.bearer.get(ue_id = 'abc', bearer_id = 1) \n
		Configures the existing bearer with the <BearerId>. \n
			:param ue_id: No help available
			:param bearer_id: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String), ArgSingle('bearer_id', bearer_id, DataType.Integer))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:UE:BEARer? {param}'.rstrip(), self.__class__.GetStruct())
