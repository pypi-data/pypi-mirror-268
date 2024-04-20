from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
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
			- Ue_Id: str: For future use. Enter any value.
			- Qos_Flow_Id: int: ID of the QoS flow to be modified.
			- Qi: enums.Qi: Optional setting parameter. 5G quality of service identifier (5QI) .
			- Max_Dl_Bitrate: int: Optional setting parameter. Maximum flow bit rate (MFBR) for the DL.
			- Max_Dl_Unit: enums.ItRateUnit: Optional setting parameter. Unit for MaxDLBitrate. Kn, Mn, Gn, Tn, Pn = n kbit/s, Mbit/s, Gbit/s, Tbit/s, Pbit/s
			- Max_Ul_Bitrate: int: Optional setting parameter. Maximum flow bit rate (MFBR) for the UL.
			- Max_Ul_Unit: enums.ItRateUnit: Optional setting parameter. Unit for MaxULBitrate.
			- Flow_Control: enums.FlowControl: Optional setting parameter. GUARanteed: GBR QoS flow NGUaranteed: non-GBR QoS flow
			- Dl_Bitrate: int: Optional setting parameter. Guaranteed flow bit rate (GFBR) for the DL, only for GBR QoS flows.
			- Dl_Unit: enums.ItRateUnit: Optional setting parameter. Unit for DLBitrate, only for GBR QoS flows.
			- Ul_Bitrate: int: Optional setting parameter. Guaranteed flow bit rate (GFBR) for the UL, only for GBR QoS flows.
			- Ul_Unit: enums.ItRateUnit: Optional setting parameter. Unit for ULBitrate, only for GBR QoS flows.
			- Averaging_Window: int or bool: Optional setting parameter. Duration over which the bit rates GFBR and MFBR are calculated for GBR QoS flows. OFF omits the parameter in the QoS flow description."""
		__meta_args_list = [
			ArgStruct.scalar_str('Ue_Id'),
			ArgStruct.scalar_int('Qos_Flow_Id'),
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
			ArgStruct.scalar_int_ext_optional('Averaging_Window')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ue_Id: str = None
			self.Qos_Flow_Id: int = None
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

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow \n
		Snippet with structure: \n
		structure = driver.configure.signaling.topology.fgs.ue.pdu.qosFlow.SetStruct() \n
		structure.Ue_Id: str = 'abc' \n
		structure.Qos_Flow_Id: int = 1 \n
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
		driver.configure.signaling.topology.fgs.ue.pdu.qosFlow.set(structure) \n
		Modifies an existing QoS flow. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Qi: enums.Qi: 5G quality of service identifier (5QI) .
			- Max_Dl_Bitrate: int: Maximum flow bit rate (MFBR) for the DL.
			- Max_Dl_Unit: enums.ItRateUnit: Unit for MaxDLBitrate. Kn, Mn, Gn, Tn, Pn = n kbit/s, Mbit/s, Gbit/s, Tbit/s, Pbit/s
			- Max_Ul_Bitrate: int: Maximum flow bit rate (MFBR) for the UL.
			- Max_Ul_Unit: enums.ItRateUnit: Unit for MaxULBitrate.
			- Flow_Control: enums.FlowControl: GUARanteed: GBR QoS flow NGUaranteed: non-GBR QoS flow
			- Dl_Bitrate: int: Guaranteed flow bit rate (GFBR) for the DL, only for GBR QoS flows.
			- Dl_Unit: enums.ItRateUnit: Unit for DLBitrate, only for GBR QoS flows.
			- Ul_Bitrate: int: Guaranteed flow bit rate (GFBR) for the UL, only for GBR QoS flows.
			- Ul_Unit: enums.ItRateUnit: Unit for ULBitrate, only for GBR QoS flows.
			- Averaging_Window: int or bool: Duration over which the bit rates GFBR and MFBR are calculated for GBR QoS flows. OFF omits the parameter in the QoS flow description."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Qi', enums.Qi),
			ArgStruct.scalar_int('Max_Dl_Bitrate'),
			ArgStruct.scalar_enum('Max_Dl_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int('Max_Ul_Bitrate'),
			ArgStruct.scalar_enum('Max_Ul_Unit', enums.ItRateUnit),
			ArgStruct.scalar_enum('Flow_Control', enums.FlowControl),
			ArgStruct.scalar_int('Dl_Bitrate'),
			ArgStruct.scalar_enum('Dl_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int('Ul_Bitrate'),
			ArgStruct.scalar_enum('Ul_Unit', enums.ItRateUnit),
			ArgStruct.scalar_int_ext('Averaging_Window')]

		def __init__(self):
			StructBase.__init__(self, self)
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

	def get(self, ue_id: str, qos_flow_id: int) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow \n
		Snippet: value: GetStruct = driver.configure.signaling.topology.fgs.ue.pdu.qosFlow.get(ue_id = 'abc', qos_flow_id = 1) \n
		Modifies an existing QoS flow. \n
			:param ue_id: For future use. Enter any value.
			:param qos_flow_id: ID of the QoS flow to be modified.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String), ArgSingle('qos_flow_id', qos_flow_id, DataType.Integer))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TOPology:FGS:UE:PDU:QOSFlow? {param}'.rstrip(), self.__class__.GetStruct())
