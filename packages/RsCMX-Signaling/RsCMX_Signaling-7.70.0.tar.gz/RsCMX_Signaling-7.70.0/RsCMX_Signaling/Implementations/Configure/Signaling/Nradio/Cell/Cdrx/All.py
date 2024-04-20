from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Enable: bool: Optional setting parameter. Enables or disables connected DRX.
			- Od_Timer: enums.OnDurationTimer: Optional setting parameter. 'drx-onDurationTimer'
			- Itimer: int: Optional setting parameter. 'drx-InactivityTimer'
			- Soffset: int: Optional setting parameter. 'drx-SlotOffset'
			- Dlhr_Timer: int: Optional setting parameter. 'drx-HARQ-RTT-TimerDL'
			- Dlr_Timer: int: Optional setting parameter. 'drx-RetransmissionTimerDL'
			- Ul_Hr_Timer: int: Optional setting parameter. 'drx-HARQ-RTT-TimerUL'
			- Ulr_Timer: int: Optional setting parameter. 'drx-RetransmissionTimerUL'
			- Ld_Rx_Cycle: int: Optional setting parameter. Duration of one long DRX cycle
			- Ld_Rx_Start_Offset: int: Optional setting parameter. 'drx-StartOffset'
			- Sd_Rx_Enable: bool: Optional setting parameter. Enables or disables short DRX cycles.
			- Sd_Rx_Cycle: int: Optional setting parameter. Duration of one short DRX cycle.
			- Sd_Rx_Sc_Timer: int: Optional setting parameter. Short cycle timer
			- Wus_Enable: bool: Optional setting parameter. Enables or disables sending DCI with format 2-6 before each long DRX cycle.
			- Wus_Mode: enums.WusMode: Optional setting parameter. Mode for sending wake-up signals. ON to OFF ratio or user-defined.
			- Wus_Ratio_On_Off: float: Optional setting parameter. Percentage of long DRX cycles for which the UE is woken up via DCI with format 2-6 containing wake-up indication = 1."""
		__meta_args_list = [
			ArgStruct.scalar_str_optional('Cell_Name'),
			ArgStruct.scalar_bool_optional('Enable'),
			ArgStruct.scalar_enum_optional('Od_Timer', enums.OnDurationTimer),
			ArgStruct.scalar_int_optional('Itimer'),
			ArgStruct.scalar_int_optional('Soffset'),
			ArgStruct.scalar_int_optional('Dlhr_Timer'),
			ArgStruct.scalar_int_optional('Dlr_Timer'),
			ArgStruct.scalar_int_optional('Ul_Hr_Timer'),
			ArgStruct.scalar_int_optional('Ulr_Timer'),
			ArgStruct.scalar_int_optional('Ld_Rx_Cycle'),
			ArgStruct.scalar_int_optional('Ld_Rx_Start_Offset'),
			ArgStruct.scalar_bool_optional('Sd_Rx_Enable'),
			ArgStruct.scalar_int_optional('Sd_Rx_Cycle'),
			ArgStruct.scalar_int_optional('Sd_Rx_Sc_Timer'),
			ArgStruct.scalar_bool_optional('Wus_Enable'),
			ArgStruct.scalar_enum_optional('Wus_Mode', enums.WusMode),
			ArgStruct.scalar_float_optional('Wus_Ratio_On_Off')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Enable: bool = None
			self.Od_Timer: enums.OnDurationTimer = None
			self.Itimer: int = None
			self.Soffset: int = None
			self.Dlhr_Timer: int = None
			self.Dlr_Timer: int = None
			self.Ul_Hr_Timer: int = None
			self.Ulr_Timer: int = None
			self.Ld_Rx_Cycle: int = None
			self.Ld_Rx_Start_Offset: int = None
			self.Sd_Rx_Enable: bool = None
			self.Sd_Rx_Cycle: int = None
			self.Sd_Rx_Sc_Timer: int = None
			self.Wus_Enable: bool = None
			self.Wus_Mode: enums.WusMode = None
			self.Wus_Ratio_On_Off: float = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.cdrx.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Enable: bool = False \n
		structure.Od_Timer: enums.OnDurationTimer = enums.OnDurationTimer.M1 \n
		structure.Itimer: int = 1 \n
		structure.Soffset: int = 1 \n
		structure.Dlhr_Timer: int = 1 \n
		structure.Dlr_Timer: int = 1 \n
		structure.Ul_Hr_Timer: int = 1 \n
		structure.Ulr_Timer: int = 1 \n
		structure.Ld_Rx_Cycle: int = 1 \n
		structure.Ld_Rx_Start_Offset: int = 1 \n
		structure.Sd_Rx_Enable: bool = False \n
		structure.Sd_Rx_Cycle: int = 1 \n
		structure.Sd_Rx_Sc_Timer: int = 1 \n
		structure.Wus_Enable: bool = False \n
		structure.Wus_Mode: enums.WusMode = enums.WusMode.RATio \n
		structure.Wus_Ratio_On_Off: float = 1.0 \n
		driver.configure.signaling.nradio.cell.cdrx.all.set(structure) \n
		Configures connected DRX settings (combination of other commands) . \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables or disables connected DRX.
			- Od_Timer: enums.OnDurationTimer: 'drx-onDurationTimer'
			- Itimer: int: 'drx-InactivityTimer'
			- Soffset: int: 'drx-SlotOffset'
			- Dlhr_Timer: int: 'drx-HARQ-RTT-TimerDL'
			- Dlr_Timer: int: 'drx-RetransmissionTimerDL'
			- Ul_Hr_Timer: int: 'drx-HARQ-RTT-TimerUL'
			- Ulr_Timer: int: 'drx-RetransmissionTimerUL'
			- Ld_Rx_Cycle: int: Duration of one long DRX cycle
			- Ld_Rx_Start_Offset: int: 'drx-StartOffset'
			- Sd_Rx_Enable: bool: Enables or disables short DRX cycles.
			- Sd_Rx_Cycle: int: Duration of one short DRX cycle.
			- Sd_Rx_Sc_Timer: int: Short cycle timer
			- Wus_Enable: bool: Enables or disables sending DCI with format 2-6 before each long DRX cycle.
			- Wus_Mode: enums.WusMode: Mode for sending wake-up signals. ON to OFF ratio or user-defined.
			- Wus_Ratio_On_Off: float: Percentage of long DRX cycles for which the UE is woken up via DCI with format 2-6 containing wake-up indication = 1."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Od_Timer', enums.OnDurationTimer),
			ArgStruct.scalar_int('Itimer'),
			ArgStruct.scalar_int('Soffset'),
			ArgStruct.scalar_int('Dlhr_Timer'),
			ArgStruct.scalar_int('Dlr_Timer'),
			ArgStruct.scalar_int('Ul_Hr_Timer'),
			ArgStruct.scalar_int('Ulr_Timer'),
			ArgStruct.scalar_int('Ld_Rx_Cycle'),
			ArgStruct.scalar_int('Ld_Rx_Start_Offset'),
			ArgStruct.scalar_bool('Sd_Rx_Enable'),
			ArgStruct.scalar_int('Sd_Rx_Cycle'),
			ArgStruct.scalar_int('Sd_Rx_Sc_Timer'),
			ArgStruct.scalar_bool('Wus_Enable'),
			ArgStruct.scalar_enum('Wus_Mode', enums.WusMode),
			ArgStruct.scalar_float('Wus_Ratio_On_Off')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Od_Timer: enums.OnDurationTimer = None
			self.Itimer: int = None
			self.Soffset: int = None
			self.Dlhr_Timer: int = None
			self.Dlr_Timer: int = None
			self.Ul_Hr_Timer: int = None
			self.Ulr_Timer: int = None
			self.Ld_Rx_Cycle: int = None
			self.Ld_Rx_Start_Offset: int = None
			self.Sd_Rx_Enable: bool = None
			self.Sd_Rx_Cycle: int = None
			self.Sd_Rx_Sc_Timer: int = None
			self.Wus_Enable: bool = None
			self.Wus_Mode: enums.WusMode = None
			self.Wus_Ratio_On_Off: float = None

	def get(self, cell_name: str = None) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CDRX:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.cdrx.all.get(cell_name = 'abc') \n
		Configures connected DRX settings (combination of other commands) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String, None, is_optional=True))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:CDRX:ALL? {param}'.rstrip(), self.__class__.GetStruct())
