from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SchedulerCls:
	"""Scheduler commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scheduler", core, parent)

	def set(self, cell_name: str, ncoherent_tpmi: enums.NcoherentTpmi, tpmi_layers: enums.MaxLength = None, tpmi: enums.Tpmi = None, resource_id: enums.ResourceId = None, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:SCHeduler \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.srs.cnCodebook.scheduler.set(cell_name = 'abc', ncoherent_tpmi = enums.NcoherentTpmi.FPARtial, tpmi_layers = enums.MaxLength.L1, tpmi = enums.Tpmi.T0, resource_id = enums.ResourceId.R1, bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param ncoherent_tpmi: No help available
			:param tpmi_layers: No help available
			:param tpmi: No help available
			:param resource_id: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ncoherent_tpmi', ncoherent_tpmi, DataType.Enum, enums.NcoherentTpmi), ArgSingle('tpmi_layers', tpmi_layers, DataType.Enum, enums.MaxLength, is_optional=True), ArgSingle('tpmi', tpmi, DataType.Enum, enums.Tpmi, is_optional=True), ArgSingle('resource_id', resource_id, DataType.Enum, enums.ResourceId, is_optional=True))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:SCHeduler {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ncoherent_Tpmi: enums.NcoherentTpmi: No parameter help available
			- Tpmi_Layers: enums.MaxLength: No parameter help available
			- Tpmi: enums.Tpmi: No parameter help available
			- Resource_Id: enums.ResourceId: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ncoherent_Tpmi', enums.NcoherentTpmi),
			ArgStruct.scalar_enum('Tpmi_Layers', enums.MaxLength),
			ArgStruct.scalar_enum('Tpmi', enums.Tpmi),
			ArgStruct.scalar_enum('Resource_Id', enums.ResourceId)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ncoherent_Tpmi: enums.NcoherentTpmi = None
			self.Tpmi_Layers: enums.MaxLength = None
			self.Tpmi: enums.Tpmi = None
			self.Resource_Id: enums.ResourceId = None

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:CNCodebook:SCHeduler \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.srs.cnCodebook.scheduler.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:CNCodebook:SCHeduler? {param}', self.__class__.GetStruct())
