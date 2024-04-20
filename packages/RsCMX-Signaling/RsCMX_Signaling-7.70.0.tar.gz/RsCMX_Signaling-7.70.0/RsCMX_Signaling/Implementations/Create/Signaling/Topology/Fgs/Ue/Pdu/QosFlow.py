from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QosFlowCls:
	"""QosFlow commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qosFlow", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Ue_Id: str: Optional setting parameter. For future use. Enter any value.
			- Pdu_Session_Id: int: Optional setting parameter. ID of the existing PDU session to which the QoS flow is added.
			- Qi: enums.Qi: Optional setting parameter. 5G quality of service identifier (5QI) .
			- Max_Dl_Bitrate: int: Optional setting parameter. Maximum flow bit rate (MFBR) for the DL.
			- Max_Dl_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 4_MaxDLBitrate. Kn, Mn, Gn, Tn, Pn = n kbit/s, Mbit/s, Gbit/s, Tbit/s, Pbit/s
			- Max_Ul_Bitrate: int: Optional setting parameter. Maximum flow bit rate (MFBR) for the UL.
			- Max_Ul_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 6_MaxULBitrate.
			- Flow_Control: enums.FlowControl: Optional setting parameter. GUARanteed: GBR QoS flow NGUaranteed: non-GBR QoS flow
			- Dl_Bitrate: int: Optional setting parameter. Guaranteed flow bit rate (GFBR) for the DL, only for GBR QoS flows.
			- Dl_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 9_DLBitrate, only for GBR QoS flows.
			- Ul_Bitrate: int: Optional setting parameter. Guaranteed flow bit rate (GFBR) for the UL, only for GBR QoS flows.
			- Ul_Unit: enums.ItRateUnit: Optional setting parameter. Unit for 11_ULBitrate, only for GBR QoS flows.
			- Averaging_Window: int or bool: Optional setting parameter. Duration over which the bit rates GFBR and MFBR are calculated for GBR QoS flows. OFF omits the parameter in the QoS flow description.
			- Rlc_Mode: enums.RlcMode: Optional setting parameter. RLC mode ACK: acknowledged UACK: unacknowledged"""
		__meta_args_list = [
			ArgStruct.scalar_str_optional('Ue_Id'),
			ArgStruct.scalar_int_optional('Pdu_Session_Id'),
			ArgStruct.scalar_enum_optional('Qi', enums.Qi),
			ArgStruct.scalar_int_optional('Max_Dl_Bitrate'),
			ArgStruct.scalar_enum_optional('Max_Dl_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_optional('Max_Ul_Bitrate'),
			ArgStruct.scalar_enum_optional('Max_Ul_Unit', enums.ItRateUnit),
			ArgStruct.scalar_enum_optional('Flow_Control', enums.FlowControl),
			ArgStruct.scalar_int_optional('Dl_Bitrate'),
			ArgStruct.scalar_enum_optional('Dl_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_optional('Ul_Bitrate'),
			ArgStruct.scalar_enum_optional('Ul_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_ext_optional('Averaging_Window'),
			ArgStruct.scalar_enum_optional('Rlc_Mode', enums.RlcMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Id: str = None
			self.Pdu_Session_Id: int = None
			self.Qi: enums.Qi = None
			self.Max_Dl_Bitrate: int = None
			self.Max_Dl_Unit: enums.ItRateUnit = None
			self.Max_Ul_Bitrate: int = None
			self.Max_Ul_Unit: enums.ItRateUnit = None
			self.Flow_Control: enums.FlowControl = None
			self.Dl_Bitrate: int = None
			self.Dl_Unit: enums.ItRateUnit = None
			self.Ul_Bitrate: int = None
			self.Ul_Unit: enums.ItRateUnit = None
			self.Averaging_Window: int or bool = None
			self.Rlc_Mode: enums.RlcMode = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow \n
		Snippet with structure: \n
		structure = driver.create.signaling.topology.fgs.ue.pdu.qosFlow.SetStruct() \n
		structure.Ue_Id: str = 'abc' \n
		structure.Pdu_Session_Id: int = 1 \n
		structure.Qi: enums.Qi = enums.Qi.Q1 \n
		structure.Max_Dl_Bitrate: int = 1 \n
		structure.Max_Dl_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Max_Ul_Bitrate: int = 1 \n
		structure.Max_Ul_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Flow_Control: enums.FlowControl = enums.FlowControl.GUARanteed \n
		structure.Dl_Bitrate: int = 1 \n
		structure.Dl_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Ul_Bitrate: int = 1 \n
		structure.Ul_Unit: enums.ItRateUnit = enums.ItRateUnit.G1 \n
		structure.Averaging_Window: int or bool = 1 \n
		structure.Rlc_Mode: enums.RlcMode = enums.RlcMode.ACK \n
		driver.create.signaling.topology.fgs.ue.pdu.qosFlow.set(structure) \n
		Adds a QoS flow to an existing PDU session. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CREate:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow', structure)
