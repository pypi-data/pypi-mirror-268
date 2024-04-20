from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import enums


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
			- Sf_Interval: int: Optional setting parameter. Subframe periodicity
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Mcs: int: No parameter help available
			- Ira: enums.Ira: Optional setting parameter. Empty transmissions before implicit release of the UL grant
			- Tic_Enable: bool: Optional setting parameter. 'twoIntervalsConfig'
			- Rv_Enable: bool: Optional setting parameter. 'fixedRV-NonAdaptive'"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int_optional('Sf_Interval'),
			ArgStruct.scalar_int_optional('Number_Rb'),
			ArgStruct.scalar_int_optional('Start_Rb'),
			ArgStruct.scalar_int_optional('Mcs'),
			ArgStruct.scalar_enum_optional('Ira', enums.Ira),
			ArgStruct.scalar_bool_optional('Tic_Enable'),
			ArgStruct.scalar_bool_optional('Rv_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Sf_Interval: int = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Mcs: int = None
			self.Ira: enums.Ira = None
			self.Tic_Enable: bool = None
			self.Rv_Enable: bool = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Sf_Interval: int = 1 \n
		structure.Number_Rb: int = 1 \n
		structure.Start_Rb: int = 1 \n
		structure.Mcs: int = 1 \n
		structure.Ira: enums.Ira = enums.Ira.E2 \n
		structure.Tic_Enable: bool = False \n
		structure.Rv_Enable: bool = False \n
		driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.all.set(structure) \n
		Configures all settings for SPS UL scheduling. A query returns the sequence <SFInterval>, <NumberRB>, <StartRB>, <MCS>,
		<TBSBits>, <IRA>, <TicEnable>, <RvEnable>. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sf_Interval: int: Subframe periodicity
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Mcs: int: No parameter help available
			- Tbs_Bits: int: No parameter help available
			- Ira: enums.Ira: Empty transmissions before implicit release of the UL grant
			- Tic_Enable: bool: 'twoIntervalsConfig'
			- Rv_Enable: bool: 'fixedRV-NonAdaptive'"""
		__meta_args_list = [
			ArgStruct.scalar_int('Sf_Interval'),
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_int('Mcs'),
			ArgStruct.scalar_int('Tbs_Bits'),
			ArgStruct.scalar_enum('Ira', enums.Ira),
			ArgStruct.scalar_bool('Tic_Enable'),
			ArgStruct.scalar_bool('Rv_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sf_Interval: int = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Mcs: int = None
			self.Tbs_Bits: int = None
			self.Ira: enums.Ira = None
			self.Tic_Enable: bool = None
			self.Rv_Enable: bool = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.all.get(cell_name = 'abc') \n
		Configures all settings for SPS UL scheduling. A query returns the sequence <SFInterval>, <NumberRB>, <StartRB>, <MCS>,
		<TBSBits>, <IRA>, <TicEnable>, <RvEnable>. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:ALL? {param}', self.__class__.GetStruct())
