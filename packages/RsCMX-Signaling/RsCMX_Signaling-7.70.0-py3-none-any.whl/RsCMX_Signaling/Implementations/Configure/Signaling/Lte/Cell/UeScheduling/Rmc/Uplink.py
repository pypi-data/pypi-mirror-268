from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def set(self, cell_name: str, enable: bool, modulation: enums.ModulationB = None, number_rb: int = None, start_rb: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:RMC:UL \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.rmc.uplink.set(cell_name = 'abc', enable = False, modulation = enums.ModulationB.BPSK, number_rb = 1, start_rb = 1) \n
		Configures LTE cell settings to values compliant with a UL RMC definition. A setting command accepts only certain value
		combinations. Use the RMC wizard in the GUI to get allowed value combinations. A query returns the set of values that are
		presented by the RMC wizard. These values can differ from currently applied values. Omit optional parameters only if you
		do not care which value you get (just any RMC-compliant value) . \n
			:param cell_name: No help available
			:param enable: Enables scheduling for all UL subframes.
			:param modulation: No help available
			:param number_rb: No help available
			:param start_rb: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean), ArgSingle('modulation', modulation, DataType.Enum, enums.ModulationB, is_optional=True), ArgSingle('number_rb', number_rb, DataType.Integer, None, is_optional=True), ArgSingle('start_rb', start_rb, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:RMC:UL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: Enables scheduling for all UL subframes.
			- Modulation: enums.ModulationB: No parameter help available
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Modulation', enums.ModulationB),
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Modulation: enums.ModulationB = None
			self.Number_Rb: int = None
			self.Start_Rb: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:RMC:UL \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.rmc.uplink.get(cell_name = 'abc') \n
		Configures LTE cell settings to values compliant with a UL RMC definition. A setting command accepts only certain value
		combinations. Use the RMC wizard in the GUI to get allowed value combinations. A query returns the set of values that are
		presented by the RMC wizard. These values can differ from currently applied values. Omit optional parameters only if you
		do not care which value you get (just any RMC-compliant value) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:RMC:UL? {param}', self.__class__.GetStruct())
