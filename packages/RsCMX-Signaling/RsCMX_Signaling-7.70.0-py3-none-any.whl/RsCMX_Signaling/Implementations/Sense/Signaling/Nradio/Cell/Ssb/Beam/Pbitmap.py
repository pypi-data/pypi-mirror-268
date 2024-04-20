from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PbitmapCls:
	"""Pbitmap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pbitmap", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Position_In_Burst: str: Bitmap, 0 = not transmitted, 1 = transmitted
			- Active_Beam_Index: int: SSB index of active beam (leftmost bit in the bitmap has index 0) ."""
		__meta_args_list = [
			ArgStruct.scalar_str('Position_In_Burst'),
			ArgStruct.scalar_int('Active_Beam_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Position_In_Burst: str = None
			self.Active_Beam_Index: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:SSB:BEAM:PBITmap \n
		Snippet: value: GetStruct = driver.sense.signaling.nradio.cell.ssb.beam.pbitmap.get(cell_name = 'abc') \n
		Queries the position bitmap, showing the time domain positions of the transmitted SS-blocks. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'SENSe:SIGNaling:NRADio:CELL:SSB:BEAM:PBITmap? {param}', self.__class__.GetStruct())
