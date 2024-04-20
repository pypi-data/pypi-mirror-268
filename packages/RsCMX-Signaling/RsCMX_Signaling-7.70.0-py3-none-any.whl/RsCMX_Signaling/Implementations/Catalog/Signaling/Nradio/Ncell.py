from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcellCls:
	"""Ncell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncell", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ncell_Name: List[str]: Neighbor cell name
			- Ncell_Type: List[enums.NcellType]: Neighbor cell type IAFRequency: intra-frequency neighbor cell IFRequency: inter-frequency neighbor cell IRAT: inter-RAT neighbor cell"""
		__meta_args_list = [
			ArgStruct('Ncell_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Ncell_Type', DataType.EnumList, enums.NcellType, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ncell_Name: List[str] = None
			self.Ncell_Type: List[enums.NcellType] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: CATalog:SIGNaling:NRADio:NCELl \n
		Snippet: value: GetStruct = driver.catalog.signaling.nradio.ncell.get(cell_name = 'abc') \n
		Queries the SIB neighbor cell list of an LTE or NR cell. For each neighbor cell, two values are returned: {<NCellName>,
		<NCellType>}cell 1, {<NCellName>, <NCellType>}cell 2, ... \n
			:param cell_name: The name of the cell for which neighbors are queried.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CATalog:SIGNaling:NRADio:NCELl? {param}', self.__class__.GetStruct())
