from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BchannelCls:
	"""Bchannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bchannel", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Fbi: int: Frequency band indicator.
			- Dl_Channel: int: No parameter help available
			- Dl_Bandwidth: enums.UlBandwidth: Optional setting parameter. Bxyz means xy.z MHz.
			- Ul_Channel: int: No parameter help available
			- Ul_Bandwidth: enums.UlBandwidth: Optional setting parameter. Bxyz means xy.z MHz."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Fbi'),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum_optional('Dl_Bandwidth', enums.UlBandwidth),
			ArgStruct.scalar_int_optional('Ul_Channel'),
			ArgStruct.scalar_enum_optional('Ul_Bandwidth', enums.UlBandwidth)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Fbi: int = None
			self.Dl_Channel: int = None
			self.Dl_Bandwidth: enums.UlBandwidth = None
			self.Ul_Channel: int = None
			self.Ul_Bandwidth: enums.UlBandwidth = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:BCHannel \n
		Snippet with structure: \n
		structure = driver.configure.signaling.lte.cell.rfSettings.bchannel.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Fbi: int = 1 \n
		structure.Dl_Channel: int = 1 \n
		structure.Dl_Bandwidth: enums.UlBandwidth = enums.UlBandwidth.B014 \n
		structure.Ul_Channel: int = 1 \n
		structure.Ul_Bandwidth: enums.UlBandwidth = enums.UlBandwidth.B014 \n
		driver.configure.signaling.lte.cell.rfSettings.bchannel.set(structure) \n
		Defines the frequency band, the channel numbers and the bandwidths. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:BCHannel', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Fbi: int: Frequency band indicator.
			- Dl_Channel: int: No parameter help available
			- Dl_Bandwidth: enums.UlBandwidth: Bxyz means xy.z MHz.
			- Ul_Channel: int: No parameter help available
			- Ul_Bandwidth: enums.UlBandwidth: Bxyz means xy.z MHz."""
		__meta_args_list = [
			ArgStruct.scalar_int('Fbi'),
			ArgStruct.scalar_int('Dl_Channel'),
			ArgStruct.scalar_enum('Dl_Bandwidth', enums.UlBandwidth),
			ArgStruct.scalar_int('Ul_Channel'),
			ArgStruct.scalar_enum('Ul_Bandwidth', enums.UlBandwidth)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fbi: int = None
			self.Dl_Channel: int = None
			self.Dl_Bandwidth: enums.UlBandwidth = None
			self.Ul_Channel: int = None
			self.Ul_Bandwidth: enums.UlBandwidth = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:BCHannel \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.rfSettings.bchannel.get(cell_name = 'abc') \n
		Defines the frequency band, the channel numbers and the bandwidths. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:BCHannel? {param}', self.__class__.GetStruct())
