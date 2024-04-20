from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FhoppingCls:
	"""Fhopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhopping", core, parent)

	def set(self, cell_name: str, resource_no: int, csrs: int, bsrs: int = None, bhop: int = None, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:ASWitching:RESource:FHOPping \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.srs.aswitching.resource.fhopping.set(cell_name = 'abc', resource_no = 1, csrs = 1, bsrs = 1, bhop = 1, bwParts = repcap.BwParts.Default) \n
		Configures the frequency hopping for SRS resource <ResourceNo> for SRS antenna switching, for BWP <bb>. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:param csrs: No help available
			:param bsrs: No help available
			:param bhop: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer), ArgSingle('csrs', csrs, DataType.Integer), ArgSingle('bsrs', bsrs, DataType.Integer, None, is_optional=True), ArgSingle('bhop', bhop, DataType.Integer, None, is_optional=True))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:ASWitching:RESource:FHOPping {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Csrs: int: No parameter help available
			- Bsrs: int: No parameter help available
			- Bhop: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Csrs'),
			ArgStruct.scalar_int('Bsrs'),
			ArgStruct.scalar_int('Bhop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Csrs: int = None
			self.Bsrs: int = None
			self.Bhop: int = None

	def get(self, cell_name: str, resource_no: int, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:ASWitching:RESource:FHOPping \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.srs.aswitching.resource.fhopping.get(cell_name = 'abc', resource_no = 1, bwParts = repcap.BwParts.Default) \n
		Configures the frequency hopping for SRS resource <ResourceNo> for SRS antenna switching, for BWP <bb>. \n
			:param cell_name: No help available
			:param resource_no: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('resource_no', resource_no, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:ASWitching:RESource:FHOPping? {param}'.rstrip(), self.__class__.GetStruct())
