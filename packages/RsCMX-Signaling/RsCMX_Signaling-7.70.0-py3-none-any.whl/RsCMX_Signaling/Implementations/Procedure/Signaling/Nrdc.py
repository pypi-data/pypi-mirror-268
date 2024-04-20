from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrdcCls:
	"""Nrdc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrdc", core, parent)

	# noinspection PyTypeChecker
	class ActivateStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Pscell: str: Optional setting parameter. Name of the second NR cell for which you want to activate NR-DC.
			- Linked_Pdu_Id: int: Optional setting parameter. ID of the existing PDU session to which the QoS flow is added.
			- Rlc_Mode: enums.RlcMode: Optional setting parameter. RLC mode ACK: acknowledged USACK: unacknowledged
			- Data_Flow: enums.DataFlow: Optional setting parameter. Configures the user data flow via the master node (MN) and the secondary node (SN) . MCG: via MN, no traffic split MCGSplit: MCG split bearer, with traffic split in the MN SCG: via SN, no traffic split SCGSplit: SCG split bearer, with traffic split in the SN
			- Traffic_Dist: float: Optional setting parameter. Configuration of a data flow with traffic split. A numeric value defines the percentage of the data to be transferred via the interface MN - UE. The remainder is transferred via the interface SN - UE. AUTO configures the traffic distribution automatically and dynamically, depending on the load in the MN path.
			- Qi: enums.Qi: Optional setting parameter. 5G quality of service identifier (5QI) .
			- Flow_Control: enums.FlowControl: Optional setting parameter. GUARanteed: GBR QoS flow NGUaranteed: non-GBR QoS flow
			- Max_Dl_Bitrate: int: Optional setting parameter. Maximum flow bit rate (MFBR) for the DL.
			- Max_Dl_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 8_MaxDlBitrate. Kn, Mn, Gn, Tn, Pn = n kbit/s, Mbit/s, Gbit/s, Tbit/s, Pbit/s
			- Max_Ul_Bitrate: int: Optional setting parameter. Maximum flow bit rate (MFBR) for the UL.
			- Max_Ul_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 10_MaxUlBitrate.
			- Dl_Bitrate: int: Optional setting parameter. Guaranteed flow bit rate (GFBR) for the DL, only for GBR QoS flows.
			- Dl_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 12_DLBitrate, only for GBR QoS flows.
			- Ul_Bitrate: int: Optional setting parameter. Guaranteed flow bit rate (GFBR) for the UL, only for GBR QoS flows.
			- Ul_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 14_ULBitrate, only for GBR QoS flows.
			- Averaging_Window: int or bool: Optional setting parameter. Duration over which the bit rates GFBR and MFBR are calculated for GBR QoS flows. OFF omits the parameter in the QoS flow description."""
		__meta_args_list = [
			ArgStruct.scalar_str_optional('Pscell'),
			ArgStruct.scalar_int_optional('Linked_Pdu_Id'),
			ArgStruct.scalar_enum_optional('Rlc_Mode', enums.RlcMode),
			ArgStruct.scalar_enum_optional('Data_Flow', enums.DataFlow),
			ArgStruct.scalar_float_optional('Traffic_Dist'),
			ArgStruct.scalar_enum_optional('Qi', enums.Qi),
			ArgStruct.scalar_enum_optional('Flow_Control', enums.FlowControl),
			ArgStruct.scalar_int_optional('Max_Dl_Bitrate'),
			ArgStruct.scalar_enum_optional('Max_Dl_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_optional('Max_Ul_Bitrate'),
			ArgStruct.scalar_enum_optional('Max_Ul_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_optional('Dl_Bitrate'),
			ArgStruct.scalar_enum_optional('Dl_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_optional('Ul_Bitrate'),
			ArgStruct.scalar_enum_optional('Ul_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_ext_optional('Averaging_Window')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pscell: str = None
			self.Linked_Pdu_Id: int = None
			self.Rlc_Mode: enums.RlcMode = None
			self.Data_Flow: enums.DataFlow = None
			self.Traffic_Dist: float = None
			self.Qi: enums.Qi = None
			self.Flow_Control: enums.FlowControl = None
			self.Max_Dl_Bitrate: int = None
			self.Max_Dl_Unit: enums.ItRateUnit = None
			self.Max_Ul_Bitrate: int = None
			self.Max_Ul_Unit: enums.ItRateUnit = None
			self.Dl_Bitrate: int = None
			self.Dl_Unit: enums.ItRateUnit = None
			self.Ul_Bitrate: int = None
			self.Ul_Unit: enums.ItRateUnit = None
			self.Averaging_Window: int or bool = None

	def activate(self, structure: ActivateStruct) -> None:
		"""SCPI: PROCedure:SIGNaling:NRDC:ACTivate \n
		Snippet with structure: \n
		structure = driver.procedure.signaling.nrdc.ActivateStruct() \n
		structure.Pscell: str = 'abc' \n
		structure.Linked_Pdu_Id: int = 1 \n
		structure.Rlc_Mode: enums.RlcMode = enums.RlcMode.ACK \n
		structure.Data_Flow: enums.DataFlow = enums.DataFlow.MCG \n
		structure.Traffic_Dist: float = 1.0 \n
		structure.Qi: enums.Qi = enums.Qi.Q1 \n
		structure.Flow_Control: enums.FlowControl = enums.FlowControl.GUARanteed \n
		structure.Max_Dl_Bitrate: int = 1 \n
		structure.Max_Dl_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Max_Ul_Bitrate: int = 1 \n
		structure.Max_Ul_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Dl_Bitrate: int = 1 \n
		structure.Dl_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Ul_Bitrate: int = 1 \n
		structure.Ul_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Averaging_Window: int or bool = 1 \n
		driver.procedure.signaling.nrdc.activate(structure) \n
		Activates the NR-DC mode and creates a QoS flow. \n
			:param structure: for set value, see the help for ActivateStruct structure arguments.
		"""
		self._core.io.write_struct(f'PROCedure:SIGNaling:NRDC:ACTivate', structure)

	def deactivate(self, pdu_session_id: int = None, qos_flow_id: int = None) -> None:
		"""SCPI: PROCedure:SIGNaling:NRDC:DEACtivate \n
		Snippet: driver.procedure.signaling.nrdc.deactivate(pdu_session_id = 1, qos_flow_id = 1) \n
		Deactivates the NR-DC mode and removes a QoS flow. \n
			:param pdu_session_id: ID of the PDU session from which the QoS flow is removed.
			:param qos_flow_id: ID of the QoS flow to be removed (QFI) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('pdu_session_id', pdu_session_id, DataType.Integer, None, is_optional=True), ArgSingle('qos_flow_id', qos_flow_id, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'PROCedure:SIGNaling:NRDC:DEACtivate {param}'.rstrip())
