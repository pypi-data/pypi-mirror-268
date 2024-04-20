from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrVersionCls:
	"""RrVersion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrVersion", core, parent)

	def set(self, cell_name: str, rep_k: enums.PdcchFormatB, rep_kr_v: enums.Spreset) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:RRVersion \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.rrVersion.set(cell_name = 'abc', rep_k = enums.PdcchFormatB.N1, rep_kr_v = enums.Spreset.S1) \n
		Configures the signaled 'repK' and 'repK-RV' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:param rep_k: No help available
			:param rep_kr_v: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('rep_k', rep_k, DataType.Enum, enums.PdcchFormatB), ArgSingle('rep_kr_v', rep_kr_v, DataType.Enum, enums.Spreset))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:RRVersion {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Rep_K: enums.PdcchFormatB: No parameter help available
			- Rep_Kr_V: enums.Spreset: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rep_K', enums.PdcchFormatB),
			ArgStruct.scalar_enum('Rep_Kr_V', enums.Spreset)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rep_K: enums.PdcchFormatB = None
			self.Rep_Kr_V: enums.Spreset = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:RRVersion \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ueScheduling.sps.uplink.rrVersion.get(cell_name = 'abc') \n
		Configures the signaled 'repK' and 'repK-RV' for UL configured grant, for the initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:UL:RRVersion? {param}', self.__class__.GetStruct())
