from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsbCls:
	"""Ssb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssb", core, parent)

	def set(self, cell_name: str, ssb_block: List[int], candidate: List[bool]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:SSB \n
		Snippet: driver.configure.signaling.nradio.cell.beam.frecovery.userDefined.ssb.set(cell_name = 'abc', ssb_block = [1, 2, 3], candidate = [True, False, True]) \n
		Specifies the SSB beam portion of a user-defined candidate list for beam failure recovery.
		See also [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE. \n
			:param cell_name: No help available
			:param ssb_block: SSB index
			:param candidate: The SSB with index SSBBlock is a candidate (ON) or not (OFF) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle.as_open_list('ssb_block', ssb_block, DataType.IntegerList, None), ArgSingle.as_open_list('candidate', candidate, DataType.BooleanList, None))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:SSB {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ssb_Block: List[int]: SSB index
			- Candidate: List[bool]: The SSB with index SSBBlock is a candidate (ON) or not (OFF) ."""
		__meta_args_list = [
			ArgStruct('Ssb_Block', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Candidate', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ssb_Block: List[int] = None
			self.Candidate: List[bool] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:SSB \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.beam.frecovery.userDefined.ssb.get(cell_name = 'abc') \n
		Specifies the SSB beam portion of a user-defined candidate list for beam failure recovery.
		See also [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:SSB? {param}', self.__class__.GetStruct())
