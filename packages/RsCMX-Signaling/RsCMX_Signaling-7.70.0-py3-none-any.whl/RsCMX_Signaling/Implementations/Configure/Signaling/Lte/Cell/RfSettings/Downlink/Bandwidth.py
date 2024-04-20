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
class BandwidthCls:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, cell_name: str, bandwidth: enums.UlBandwidth) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:DL:BWIDth \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.downlink.bandwidth.set(cell_name = 'abc', bandwidth = enums.UlBandwidth.B014) \n
		Selects the channel bandwidth for the downlink. Configure the same value for DL and UL. A query returns <Bandwidth>,
		<ResourceBlocks>. \n
			:param cell_name: No help available
			:param bandwidth: Bxyz means xy.z MHz.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('bandwidth', bandwidth, DataType.Enum, enums.UlBandwidth))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:DL:BWIDth {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Bandwidth: enums.UlBandwidth: Bxyz means xy.z MHz.
			- Resource_Blocks: int: Number of allocated resource blocks (full allocation of the bandwidth) ."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bandwidth', enums.UlBandwidth),
			ArgStruct.scalar_int('Resource_Blocks')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bandwidth: enums.UlBandwidth = None
			self.Resource_Blocks: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:DL:BWIDth \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.rfSettings.downlink.bandwidth.get(cell_name = 'abc') \n
		Selects the channel bandwidth for the downlink. Configure the same value for DL and UL. A query returns <Bandwidth>,
		<ResourceBlocks>. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:DL:BWIDth? {param}', self.__class__.GetStruct())
