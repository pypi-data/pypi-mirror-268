from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoCls:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ta_Code: str: Tracking area code (TAC) .
			- Count_Cells_Lte: int: Number of associated LTE cells.
			- Count_Cells_Nr: int: Number of associated NR cells.
			- List_Of_Cells_Lte: str: Comma-separated list of strings, one string per LTE cell (name of the cell) . If there are no LTE cells, an empty string is returned.
			- List_Of_Cells_Nr: str: Comma-separated list of strings, one string per NR cell (name of the cell) . If there are no NR cells, an empty string is returned."""
		__meta_args_list = [
			ArgStruct.scalar_str('Ta_Code'),
			ArgStruct.scalar_int('Count_Cells_Lte'),
			ArgStruct.scalar_int('Count_Cells_Nr'),
			ArgStruct.scalar_str('List_Of_Cells_Lte'),
			ArgStruct.scalar_str('List_Of_Cells_Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ta_Code: str = None
			self.Count_Cells_Lte: int = None
			self.Count_Cells_Nr: int = None
			self.List_Of_Cells_Lte: str = None
			self.List_Of_Cells_Nr: str = None

	def get(self, name_ta_5_g: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:FGS:INFO \n
		Snippet: value: GetStruct = driver.configure.signaling.topology.fgs.info.get(name_ta_5_g = 'abc') \n
		Queries basic information about a 5GS tracking area. \n
			:param name_ta_5_g: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name_ta_5_g)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TOPology:FGS:INFO? {param}', self.__class__.GetStruct())
