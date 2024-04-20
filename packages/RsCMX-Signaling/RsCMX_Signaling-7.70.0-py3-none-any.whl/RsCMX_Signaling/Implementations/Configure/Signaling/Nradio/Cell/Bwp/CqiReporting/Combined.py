from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


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
			- Enable: enums.EnableCqi: No parameter help available
			- Periodicity: enums.PeriodicityCqiReport: No parameter help available
			- Offset: int: No parameter help available
			- Ports: enums.Ports: No parameter help available
			- Symbol: int: No parameter help available
			- Power: enums.RsrcPower: No parameter help available
			- Report_Offset: int: No parameter help available
			- Report_Cqi: enums.ReportCqi: No parameter help available
			- Report_Pmi: enums.ReportCqi: No parameter help available"""
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

	def set(self, structure: SetStruct, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:COMBined \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.bwp.cqiReporting.combined.SetStruct() \n
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
		driver.configure.signaling.nradio.cell.bwp.cqiReporting.combined.set(structure, bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:COMBined', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: enums.EnableCqi: No parameter help available
			- Periodicity: enums.PeriodicityCqiReport: No parameter help available
			- Offset: int: No parameter help available
			- Ports: enums.Ports: No parameter help available
			- Symbol: int: No parameter help available
			- Power: enums.RsrcPower: No parameter help available
			- Report_Offset: int: No parameter help available
			- Report_Cqi: enums.ReportCqi: No parameter help available
			- Report_Pmi: enums.ReportCqi: No parameter help available"""
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

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:COMBined \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.cqiReporting.combined.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:COMBined? {param}', self.__class__.GetStruct())
