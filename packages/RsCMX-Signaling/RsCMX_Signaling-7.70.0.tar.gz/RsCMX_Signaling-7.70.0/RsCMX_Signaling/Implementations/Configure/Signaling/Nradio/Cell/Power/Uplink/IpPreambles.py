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
class IpPreamblesCls:
	"""IpPreambles commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipPreambles", core, parent)

	def set(self, cell_name: str, ignore_prach_mode: enums.IgnorePrachMode, no_ignored: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:IPPReambles \n
		Snippet: driver.configure.signaling.nradio.cell.power.uplink.ipPreambles.set(cell_name = 'abc', ignore_prach_mode = enums.IgnorePrachMode.IALLways, no_ignored = 1) \n
		Selects the behavior of the signaling application when receiving preambles from the UE. The setting is synchronized over
		all NR cells (identical values for all NR cells) . \n
			:param cell_name: No help available
			:param ignore_prach_mode: IALLways: ignore all preambles IXTimes: ignore NoIgnored preambles RALLways: respond to all preambles
			:param no_ignored: Number of preambles to be ignored for IgnorePrachMode = IXTimes.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ignore_prach_mode', ignore_prach_mode, DataType.Enum, enums.IgnorePrachMode), ArgSingle('no_ignored', no_ignored, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:IPPReambles {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ignore_Prach_Mode: enums.IgnorePrachMode: IALLways: ignore all preambles IXTimes: ignore NoIgnored preambles RALLways: respond to all preambles
			- No_Ignored: int: Number of preambles to be ignored for IgnorePrachMode = IXTimes."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ignore_Prach_Mode', enums.IgnorePrachMode),
			ArgStruct.scalar_int('No_Ignored')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ignore_Prach_Mode: enums.IgnorePrachMode = None
			self.No_Ignored: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:UL:IPPReambles \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.power.uplink.ipPreambles.get(cell_name = 'abc') \n
		Selects the behavior of the signaling application when receiving preambles from the UE. The setting is synchronized over
		all NR cells (identical values for all NR cells) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:POWer:UL:IPPReambles? {param}', self.__class__.GetStruct())
