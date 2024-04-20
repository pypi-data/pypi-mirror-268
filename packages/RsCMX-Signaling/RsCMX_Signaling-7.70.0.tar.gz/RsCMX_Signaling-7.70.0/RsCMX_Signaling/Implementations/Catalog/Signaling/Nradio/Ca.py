from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaCls:
	"""Ca commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ca", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Pcell_Name: str: Name of the PCell or PSCell of the cell group.
			- Scell_Name: List[str]: Name of an SCell of the cell group."""
		__meta_args_list = [
			ArgStruct.scalar_str('Pcell_Name'),
			ArgStruct('Scell_Name', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pcell_Name: str = None
			self.Scell_Name: List[str] = None

	def get(self, cell_group_name: str) -> GetStruct:
		"""SCPI: CATalog:SIGNaling:NRADio:CA \n
		Snippet: value: GetStruct = driver.catalog.signaling.nradio.ca.get(cell_group_name = 'abc') \n
		Queries a list of all cells contained in a specific LTE or NR cell group. The first returned cell is a primary cell. The
		other cells are secondary cells: <PCellName>, <SCellName>1, ..., <SCellName>n \n
			:param cell_group_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_group_name)
		return self._core.io.query_struct(f'CATalog:SIGNaling:NRADio:CA? {param}', self.__class__.GetStruct())
