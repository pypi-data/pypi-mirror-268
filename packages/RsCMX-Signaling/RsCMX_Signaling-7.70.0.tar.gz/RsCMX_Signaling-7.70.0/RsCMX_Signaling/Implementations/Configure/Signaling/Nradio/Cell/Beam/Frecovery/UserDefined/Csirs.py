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
class CsirsCls:
	"""Csirs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirs", core, parent)

	def set(self, cell_name: str, nzb_id: List[int], candidate: List[bool]) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:CSIRs \n
		Snippet: driver.configure.signaling.nradio.cell.beam.frecovery.userDefined.csirs.set(cell_name = 'abc', nzb_id = [1, 2, 3], candidate = [True, False, True]) \n
		Specifies the CSI-RS part of a user-defined candidate list for beam failure recovery.
		See also [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE. \n
			:param cell_name: No help available
			:param nzb_id: NZP CSI-RS resource index
			:param candidate: The CSI-RS beam with index NZBId is a candidate (ON) or not (OFF) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle.as_open_list('nzb_id', nzb_id, DataType.IntegerList, None), ArgSingle.as_open_list('candidate', candidate, DataType.BooleanList, None))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:CSIRs {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Nzb_Id: List[int]: NZP CSI-RS resource index
			- Candidate: List[bool]: The CSI-RS beam with index NZBId is a candidate (ON) or not (OFF) ."""
		__meta_args_list = [
			ArgStruct('Nzb_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Candidate', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nzb_Id: List[int] = None
			self.Candidate: List[bool] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:CSIRs \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.beam.frecovery.userDefined.csirs.get(cell_name = 'abc') \n
		Specifies the CSI-RS part of a user-defined candidate list for beam failure recovery.
		See also [CONFigure:]SIGNaling:NRADio:CELL:BEAM:FRECovery:MODE. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BEAM:FRECovery:UDEFined:CSIRs? {param}', self.__class__.GetStruct())
