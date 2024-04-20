from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CombinedCls:
	"""Combined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("combined", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Enable: enums.EnableCqi: Optional setting parameter. Selects the CSI reporting type. OFF: no reporting PERiodic: periodic CSI reporting APERiodic: aperiodic CSI reporting SPERsistant: semi-persistent CSI reporting
			- Periodicity: enums.PeriodicityCqiReport: Optional setting parameter. Global periodicity for CSI reporting and CSI-RS resources, in slots.
			- Offset: int: Optional setting parameter. Offset value of 'periodicityAndOffset' in IE 'NZP-CSI-RS-Resource'. The offset must be less than the periodicity.
			- Ports: enums.Ports: Optional setting parameter. The number of CSI-RS ports that is signaled as 'nrofPorts' in IE 'CSI-RS-ResourceMapping'.
			- Symbol: int: Optional setting parameter. The first OFDM symbol in the RB used for CSI-RS.
			- Power: enums.RsrcPower: Optional setting parameter. Power offset of NZP CSI-RS RE to SSS RE. -9 dB, -6 dB, -3 dB, 0 dB, +3 dB, +6 dB
			- Report_Offset: int: Optional setting parameter. Offset value of 'reportSlotConfig'. The offset must be less than the periodicity.
			- Report_Cqi: enums.ReportCqi: Optional setting parameter. 'cqi-FormatIndicator' signaled to the UE. OFF: no CQI reporting WB: wideband CQI reporting SB: subband CQI reporting
			- Report_Pmi: enums.ReportCqi: Optional setting parameter. 'pmi-FormatIndicator' signaled to the UE. OFF: no PMI reporting WB: wideband PMI reporting SB: subband PMI reporting"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum_optional('Enable', enums.EnableCqi),
			ArgStruct.scalar_enum_optional('Periodicity', enums.PeriodicityCqiReport),
			ArgStruct.scalar_int_optional('Offset'),
			ArgStruct.scalar_enum_optional('Ports', enums.Ports),
			ArgStruct.scalar_int_optional('Symbol'),
			ArgStruct.scalar_enum_optional('Power', enums.RsrcPower),
			ArgStruct.scalar_int_optional('Report_Offset'),
			ArgStruct.scalar_enum_optional('Report_Cqi', enums.ReportCqi),
			ArgStruct.scalar_enum_optional('Report_Pmi', enums.ReportCqi)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Enable: enums.EnableCqi = None
			self.Periodicity: enums.PeriodicityCqiReport = None
			self.Offset: int = None
			self.Ports: enums.Ports = None
			self.Symbol: int = None
			self.Power: enums.RsrcPower = None
			self.Report_Offset: int = None
			self.Report_Cqi: enums.ReportCqi = None
			self.Report_Pmi: enums.ReportCqi = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:COMBined \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.cqiReporting.combined.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Enable: enums.EnableCqi = enums.EnableCqi.APERiodic \n
		structure.Periodicity: enums.PeriodicityCqiReport = enums.PeriodicityCqiReport.P10 \n
		structure.Offset: int = 1 \n
		structure.Ports: enums.Ports = enums.Ports.P1 \n
		structure.Symbol: int = 1 \n
		structure.Power: enums.RsrcPower = enums.RsrcPower.M3DB \n
		structure.Report_Offset: int = 1 \n
		structure.Report_Cqi: enums.ReportCqi = enums.ReportCqi.OFF \n
		structure.Report_Pmi: enums.ReportCqi = enums.ReportCqi.OFF \n
		driver.configure.signaling.nradio.cell.cqiReporting.combined.set(structure) \n
		Configures several CQI reporting settings simultaneously. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:COMBined', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: enums.EnableCqi: Selects the CSI reporting type. OFF: no reporting PERiodic: periodic CSI reporting APERiodic: aperiodic CSI reporting SPERsistant: semi-persistent CSI reporting
			- Periodicity: enums.PeriodicityCqiReport: Global periodicity for CSI reporting and CSI-RS resources, in slots.
			- Offset: int: Offset value of 'periodicityAndOffset' in IE 'NZP-CSI-RS-Resource'. The offset must be less than the periodicity.
			- Ports: enums.Ports: The number of CSI-RS ports that is signaled as 'nrofPorts' in IE 'CSI-RS-ResourceMapping'.
			- Symbol: int: The first OFDM symbol in the RB used for CSI-RS.
			- Power: enums.RsrcPower: Power offset of NZP CSI-RS RE to SSS RE. -9 dB, -6 dB, -3 dB, 0 dB, +3 dB, +6 dB
			- Report_Offset: int: Offset value of 'reportSlotConfig'. The offset must be less than the periodicity.
			- Report_Cqi: enums.ReportCqi: 'cqi-FormatIndicator' signaled to the UE. OFF: no CQI reporting WB: wideband CQI reporting SB: subband CQI reporting
			- Report_Pmi: enums.ReportCqi: 'pmi-FormatIndicator' signaled to the UE. OFF: no PMI reporting WB: wideband PMI reporting SB: subband PMI reporting"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Enable', enums.EnableCqi),
			ArgStruct.scalar_enum('Periodicity', enums.PeriodicityCqiReport),
			ArgStruct.scalar_int('Offset'),
			ArgStruct.scalar_enum('Ports', enums.Ports),
			ArgStruct.scalar_int('Symbol'),
			ArgStruct.scalar_enum('Power', enums.RsrcPower),
			ArgStruct.scalar_int('Report_Offset'),
			ArgStruct.scalar_enum('Report_Cqi', enums.ReportCqi),
			ArgStruct.scalar_enum('Report_Pmi', enums.ReportCqi)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: enums.EnableCqi = None
			self.Periodicity: enums.PeriodicityCqiReport = None
			self.Offset: int = None
			self.Ports: enums.Ports = None
			self.Symbol: int = None
			self.Power: enums.RsrcPower = None
			self.Report_Offset: int = None
			self.Report_Cqi: enums.ReportCqi = None
			self.Report_Pmi: enums.ReportCqi = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:COMBined \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.cqiReporting.combined.get(cell_name = 'abc') \n
		Configures several CQI reporting settings simultaneously. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:COMBined? {param}', self.__class__.GetStruct())
