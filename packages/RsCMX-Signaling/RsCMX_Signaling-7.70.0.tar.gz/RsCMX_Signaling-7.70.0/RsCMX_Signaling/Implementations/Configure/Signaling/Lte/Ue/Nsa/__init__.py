from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NsaCls:
	"""Nsa commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsa", core, parent)

	@property
	def resume(self):
		"""resume commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resume'):
			from .Resume import ResumeCls
			self._resume = ResumeCls(self._core, self._cmd_group)
		return self._resume

	# noinspection PyTypeChecker
	class ActivateStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Ue_Id: str: Optional setting parameter. For future use. Enter any value if you want to use optional parameters.
			- Linked_Bearer_Id: int: Optional setting parameter. ID of the default bearer to which the dedicated bearer is linked. To get a list of all default bearer IDs, see [CMDLINKRESOLVED Catalog.Signaling.Lte.Ue.Dbearer#get_ CMDLINKRESOLVED].
			- Data_Flow: enums.DataFlow: Optional setting parameter. Configures the user data flow for the dedicated bearer. MCGSplit: MCG split bearer, with traffic split in the eNB SCG: SCG via gNB, no traffic split SCGSplit: SCG split bearer, with traffic split in the gNB
			- Traffic_Dist: float: Optional setting parameter. For MCGSplit and SCGSplit. A numeric value defines the percentage of the data to be transferred via the interface eNB - UE. The remainder is transferred via the interface gNB - UE. AUTO configures the traffic distribution automatically and dynamically, depending on the load in the eNB path.
			- Qci: enums.Qi: Optional setting parameter. Value of the quality of service class identifier. Values defined in 3GPP TS 23.203, table 6.1.7. The GUI shows the designation of each value.
			- Max_Dl_Bitrate: int: Optional setting parameter. Maximum DL bit rate allowed in the network.
			- Max_Ul_Bitrate: int: Optional setting parameter. Maximum UL bit rate allowed in the network.
			- Gtd_Dl_Bitrate: int: Optional setting parameter. DL bit rate guaranteed by the network for the bearer.
			- Gtd_Ul_Bitrate: int: Optional setting parameter. UL bit rate guaranteed by the network for the bearer.
			- Pscell: str: Optional setting parameter. Name of the NR cell for which you want to activate EN-DC.
			- Rlc_Mode: enums.RlcMode: Optional setting parameter. RLC mode ACK: acknowledged UACK: unacknowledged"""
		__meta_args_list = [
			ArgStruct.scalar_str_optional('Ue_Id'),
			ArgStruct.scalar_int_optional('Linked_Bearer_Id'),
			ArgStruct.scalar_enum_optional('Data_Flow', enums.DataFlow),
			ArgStruct.scalar_float_optional('Traffic_Dist'),
			ArgStruct.scalar_enum_optional('Qci', enums.Qi),
			ArgStruct.scalar_int_optional('Max_Dl_Bitrate'),
			ArgStruct.scalar_int_optional('Max_Ul_Bitrate'),
			ArgStruct.scalar_int_optional('Gtd_Dl_Bitrate'),
			ArgStruct.scalar_int_optional('Gtd_Ul_Bitrate'),
			ArgStruct.scalar_str_optional('Pscell'),
			ArgStruct.scalar_enum_optional('Rlc_Mode', enums.RlcMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Id: str = None
			self.Linked_Bearer_Id: int = None
			self.Data_Flow: enums.DataFlow = None
			self.Traffic_Dist: float = None
			self.Qci: enums.Qi = None
			self.Max_Dl_Bitrate: int = None
			self.Max_Ul_Bitrate: int = None
			self.Gtd_Dl_Bitrate: int = None
			self.Gtd_Ul_Bitrate: int = None
			self.Pscell: str = None
			self.Rlc_Mode: enums.RlcMode = None

	def activate(self, structure: ActivateStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:NSA:ACTivate \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.ue.nsa.ActivateStruct() \n
		structure.Ue_Id: str = 'abc' \n
		structure.Linked_Bearer_Id: int = 1 \n
		structure.Data_Flow: enums.DataFlow = enums.DataFlow.MCG \n
		structure.Traffic_Dist: float = 1.0 \n
		structure.Qci: enums.Qi = enums.Qi.Q1 \n
		structure.Max_Dl_Bitrate: int = 1 \n
		structure.Max_Ul_Bitrate: int = 1 \n
		structure.Gtd_Dl_Bitrate: int = 1 \n
		structure.Gtd_Ul_Bitrate: int = 1 \n
		structure.Pscell: str = 'abc' \n
		structure.Rlc_Mode: enums.RlcMode = enums.RlcMode.ACK \n
		driver.configure.signaling.lte.ue.nsa.activate(structure) \n
		Activates the EN-DC mode and establishes a dedicated bearer. \n
			:param structure: for set value, see the help for ActivateStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:UE:NSA:ACTivate', structure)

	def deactivate(self, ue_id: str = None, bearer_id: int = None, esm_cause: enums.EsmCause = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:UE:NSA:DEACtivate \n
		Snippet: driver.configure.signaling.lte.ue.nsa.deactivate(ue_id = 'abc', bearer_id = 1, esm_cause = enums.EsmCause.C100) \n
		Deactivates the EN-DC mode and releases a dedicated bearer. \n
			:param ue_id: For future use. Enter any value if you want to use optional parameters.
			:param bearer_id: ID of the dedicated bearer to be released. To get a list of all dedicated bearer IDs, see method RsCMX_Signaling.Catalog.Signaling.Lte.Ue.Bearer.get_.
			:param esm_cause: Release cause to be sent. Values defined in 3GPP TS 24.301, chapter 9.9.4.4.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True), ArgSingle('bearer_id', bearer_id, DataType.Integer, None, is_optional=True), ArgSingle('esm_cause', esm_cause, DataType.Enum, enums.EsmCause, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:UE:NSA:DEACtivate {param}'.rstrip())

	def clone(self) -> 'NsaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NsaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
