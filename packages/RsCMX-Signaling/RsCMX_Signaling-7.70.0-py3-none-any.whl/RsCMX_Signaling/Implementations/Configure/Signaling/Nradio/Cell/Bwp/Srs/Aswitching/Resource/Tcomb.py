from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcombCls:
	"""Tcomb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcomb", core, parent)

	def set(self, cell_name: str, resource_no: int, ktc: enums.Ktc = None, offset: int = None, cyclic_shift: int = None, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:ASWitching:RESource:TCOMb \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.srs.aswitching.resource.tcomb.set(cell_name = 'abc', resource_no = 1, ktc = enums.Ktc.N2, offset = 1, cyclic_shift = 1, bwParts = repcap.BwParts.Default) \n
		Configures the comb structure of the SRS resource <ResourceNo> for SRS antenna switching, for BWP <bb>. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:param ktc: No help available
			:param offset: No help available
			:param cyclic_shift: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer), ArgSingle('ktc', ktc, DataType.Enum, enums.Ktc, is_optional=True), ArgSingle('offset', offset, DataType.Integer, None, is_optional=True), ArgSingle('cyclic_shift', cyclic_shift, DataType.Integer, None, is_optional=True))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:ASWitching:RESource:TCOMb {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ktc: enums.Ktc: No parameter help available
			- Offset: int: No parameter help available
			- Cyclic_Shift: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ktc', enums.Ktc),
			ArgStruct.scalar_int('Offset'),
			ArgStruct.scalar_int('Cyclic_Shift')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ktc: enums.Ktc = None
			self.Offset: int = None
			self.Cyclic_Shift: int = None

	def get(self, cell_name: str, resource_no: int, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:ASWitching:RESource:TCOMb \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.srs.aswitching.resource.tcomb.get(cell_name = 'abc', resource_no = 1, bwParts = repcap.BwParts.Default) \n
		Configures the comb structure of the SRS resource <ResourceNo> for SRS antenna switching, for BWP <bb>. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:ASWitching:RESource:TCOMb? {param}'.rstrip(), self.__class__.GetStruct())
