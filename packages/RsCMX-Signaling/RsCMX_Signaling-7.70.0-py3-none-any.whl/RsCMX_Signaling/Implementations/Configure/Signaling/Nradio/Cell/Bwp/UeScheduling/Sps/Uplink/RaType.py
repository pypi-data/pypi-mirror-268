from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RaTypeCls:
	"""RaType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("raType", core, parent)

	def set(self, cell_name: str, resource_allocation_type: enums.ResourceAllocationType, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:UL:RATYpe \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.uplink.raType.set(cell_name = 'abc', resource_allocation_type = enums.ResourceAllocationType.DSWich, bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'resourceAllocation' for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param resource_allocation_type: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_allocation_type', resource_allocation_type, DataType.Enum, enums.ResourceAllocationType))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:UL:RATYpe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.ResourceAllocationType:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:UL:RATYpe \n
		Snippet: value: enums.ResourceAllocationType = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.uplink.raType.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'resourceAllocation' for UL configured grant, for BWP <bb>. \n
			:param cell_name: type 0, type 1, dynamic switch
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: resource_allocation_type: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:UL:RATYpe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ResourceAllocationType)
