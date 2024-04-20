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
			- Mcc: str: No parameter help available
			- Mnc: str: No parameter help available
			- Count_Ta_Eps: int: Number of associated EPS tracking areas.
			- Count_Ta_5_G: int: Number of associated 5GS tracking areas.
			- List_Name_Ta_Eps: str: Comma-separated list of strings, one string per EPS tracking area (name of the EPS TA) . If there are no EPS TAs, an empty string is returned.
			- List_Name_5_G: str: Comma-separated list of strings, one string per 5GS tracking area (name of the 5GS TA) . If there are no 5GS TAs, an empty string is returned."""
		__meta_args_list = [
			ArgStruct.scalar_str('Mcc'),
			ArgStruct.scalar_str('Mnc'),
			ArgStruct.scalar_int('Count_Ta_Eps'),
			ArgStruct.scalar_int('Count_Ta_5_G'),
			ArgStruct.scalar_str('List_Name_Ta_Eps'),
			ArgStruct.scalar_str('List_Name_5_G')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcc: str = None
			self.Mnc: str = None
			self.Count_Ta_Eps: int = None
			self.Count_Ta_5_G: int = None
			self.List_Name_Ta_Eps: str = None
			self.List_Name_5_G: str = None

	def get(self, name_plmn: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:TOPology:PLMN:INFO \n
		Snippet: value: GetStruct = driver.configure.signaling.topology.plmn.info.get(name_plmn = 'abc') \n
		Queries basic information about a PLMN. \n
			:param name_plmn: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(name_plmn)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:TOPology:PLMN:INFO? {param}', self.__class__.GetStruct())
