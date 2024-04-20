from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	def set(self, name_ta: str, name_plmn: str, ta_code: int = None, time_3412: float = None) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:EPS \n
		Snippet: driver.create.signaling.topology.eps.set(name_ta = 'abc', name_plmn = 'abc', ta_code = 1, time_3412 = 1.0) \n
		Creates an EPS tracking area in a selected PLMN and optionally defines tracking area settings. Assign a unique name to
		each named object within the test environment. Assigning an already used name can be rejected with an error message, even
		if the other object has not the same type as the new object. \n
			:param name_ta: Assigns a name to the tracking area. The string is used in other commands to select this tracking area.
			:param name_plmn: PLMN containing the tracking area.
			:param ta_code: Tracking area code (TAC) .
			:param time_3412: No effect - for future use.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta', name_ta, DataType.String), ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('ta_code', ta_code, DataType.Integer, None, is_optional=True), ArgSingle('time_3412', time_3412, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CREate:SIGNaling:TOPology:EPS {param}'.rstrip())

	# noinspection PyTypeChecker
	class BearerStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Linked_Bearer_Id: int: ID of the default bearer to which the dedicated bearer is linked. To get a list of all default bearer IDs, see [CMDLINKRESOLVED Catalog.Signaling.Lte.Ue.Dbearer#get_ CMDLINKRESOLVED].
			- Qci: enums.Qi: Optional setting parameter. Value of the quality of service class identifier. Values defined in 3GPP TS 23.203, table 6.1.7. The GUI shows the designation of each value.
			- Rlc_Mode: enums.RlcMode: Optional setting parameter. ACK: acknowledged UACK: unacknowledged
			- Max_Dl_Bitrate: int: Optional setting parameter. Maximum DL bit rate allowed in the network.
			- Max_Ul_Bitrate: int: Optional setting parameter. Maximum UL bit rate allowed in the network.
			- Gtd_Dl_Bitrate: int: Optional setting parameter. DL bit rate guaranteed by the network for the bearer.
			- Gtd_Ul_Bitrate: int: Optional setting parameter. UL bit rate guaranteed by the network for the bearer.
			- Local_Port_Lower: int: Optional setting parameter. The minimum of the local port range in the traffic flow template.
			- Local_Port_Upper: int: Optional setting parameter. The maximum of the local port range in the traffic flow template.
			- Remote_Port_Lower: int: Optional setting parameter. The minimum of the remote port range in the traffic flow template.
			- Remote_Port_Upper: int: Optional setting parameter. The maximum of the remote port range in the traffic flow template."""
		__meta_args_list = [
			ArgStruct.scalar_int('Linked_Bearer_Id'),
			ArgStruct.scalar_enum_optional('Qci', enums.Qi),
			ArgStruct.scalar_enum_optional('Rlc_Mode', enums.RlcMode),
			ArgStruct.scalar_int_optional('Max_Dl_Bitrate'),
			ArgStruct.scalar_int_optional('Max_Ul_Bitrate'),
			ArgStruct.scalar_int_optional('Gtd_Dl_Bitrate'),
			ArgStruct.scalar_int_optional('Gtd_Ul_Bitrate'),
			ArgStruct.scalar_int_optional('Local_Port_Lower'),
			ArgStruct.scalar_int_optional('Local_Port_Upper'),
			ArgStruct.scalar_int_optional('Remote_Port_Lower'),
			ArgStruct.scalar_int_optional('Remote_Port_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Linked_Bearer_Id: int = None
			self.Qci: enums.Qi = None
			self.Rlc_Mode: enums.RlcMode = None
			self.Max_Dl_Bitrate: int = None
			self.Max_Ul_Bitrate: int = None
			self.Gtd_Dl_Bitrate: int = None
			self.Gtd_Ul_Bitrate: int = None
			self.Local_Port_Lower: int = None
			self.Local_Port_Upper: int = None
			self.Remote_Port_Lower: int = None
			self.Remote_Port_Upper: int = None

	def set_bearer(self, value: BearerStruct) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:EPS:BEARer \n
		Snippet with structure: \n
		structure = driver.create.signaling.topology.eps.BearerStruct() \n
		structure.Linked_Bearer_Id: int = 1 \n
		structure.Qci: enums.Qi = enums.Qi.Q1 \n
		structure.Rlc_Mode: enums.RlcMode = enums.RlcMode.ACK \n
		structure.Max_Dl_Bitrate: int = 1 \n
		structure.Max_Ul_Bitrate: int = 1 \n
		structure.Gtd_Dl_Bitrate: int = 1 \n
		structure.Gtd_Ul_Bitrate: int = 1 \n
		structure.Local_Port_Lower: int = 1 \n
		structure.Local_Port_Upper: int = 1 \n
		structure.Remote_Port_Lower: int = 1 \n
		structure.Remote_Port_Upper: int = 1 \n
		driver.create.signaling.topology.eps.set_bearer(value = structure) \n
		Establishes a dedicated bearer. \n
			:param value: see the help for BearerStruct structure arguments.
		"""
		self._core.io.write_struct('CREate:SIGNaling:TOPology:EPS:BEARer', value)
