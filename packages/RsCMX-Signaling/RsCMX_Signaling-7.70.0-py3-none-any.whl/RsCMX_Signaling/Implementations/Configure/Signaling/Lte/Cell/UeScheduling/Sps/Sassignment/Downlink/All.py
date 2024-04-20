from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, cell_name: str, sf_interval: int = None, number_rb: int = None, start_rb: int = None, mcs: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:ALL \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.downlink.all.set(cell_name = 'abc', sf_interval = 1, number_rb = 1, start_rb = 1, mcs = 1) \n
		Configures all settings for SPS DL scheduling. A query returns the sequence <SFInterval>, <NumberRB>, <StartRB>, <MCS>,
		<TBSBits>. \n
			:param cell_name: No help available
			:param sf_interval: Subframe periodicity
			:param number_rb: No help available
			:param start_rb: No help available
			:param mcs: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('sf_interval', sf_interval, DataType.Integer, None, is_optional=True), ArgSingle('number_rb', number_rb, DataType.Integer, None, is_optional=True), ArgSingle('start_rb', start_rb, DataType.Integer, None, is_optional=True), ArgSingle('mcs', mcs, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sf_Interval: int: Subframe periodicity
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Mcs: int: No parameter help available
			- Tbs_Bits: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Sf_Interval'),
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_int('Mcs'),
			ArgStruct.scalar_int('Tbs_Bits')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sf_Interval: int = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Mcs: int = None
			self.Tbs_Bits: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.downlink.all.get(cell_name = 'abc') \n
		Configures all settings for SPS DL scheduling. A query returns the sequence <SFInterval>, <NumberRB>, <StartRB>, <MCS>,
		<TBSBits>. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:DL:ALL? {param}', self.__class__.GetStruct())
