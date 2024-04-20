from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcandidatesCls:
	"""Ncandidates commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncandidates", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Aggr_Level_1: enums.AggrLevel: No parameter help available
			- Aggr_Level_2: enums.AggrLevel: No parameter help available
			- Aggr_Level_4: enums.AggrLevel: No parameter help available
			- Aggr_Level_8: enums.AggrLevel: No parameter help available
			- Aggr_Level_16: enums.AggrLevel: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_enum('Aggr_Level_1', enums.AggrLevel),
			ArgStruct.scalar_enum_optional('Aggr_Level_2', enums.AggrLevel),
			ArgStruct.scalar_enum_optional('Aggr_Level_4', enums.AggrLevel),
			ArgStruct.scalar_enum_optional('Aggr_Level_8', enums.AggrLevel),
			ArgStruct.scalar_enum_optional('Aggr_Level_16', enums.AggrLevel)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Aggr_Level_1: enums.AggrLevel = None
			self.Aggr_Level_2: enums.AggrLevel = None
			self.Aggr_Level_4: enums.AggrLevel = None
			self.Aggr_Level_8: enums.AggrLevel = None
			self.Aggr_Level_16: enums.AggrLevel = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:COReset:NCANdidates \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.ibwp.coreset.ncandidates.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Aggr_Level_1: enums.AggrLevel = enums.AggrLevel.N0 \n
		structure.Aggr_Level_2: enums.AggrLevel = enums.AggrLevel.N0 \n
		structure.Aggr_Level_4: enums.AggrLevel = enums.AggrLevel.N0 \n
		structure.Aggr_Level_8: enums.AggrLevel = enums.AggrLevel.N0 \n
		structure.Aggr_Level_16: enums.AggrLevel = enums.AggrLevel.N0 \n
		driver.configure.signaling.nradio.cell.ibwp.coreset.ncandidates.set(structure) \n
		Configures the number of PDCCH candidates per aggregation level. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:COReset:NCANdidates', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Aggr_Level_1: enums.AggrLevel: No parameter help available
			- Aggr_Level_2: enums.AggrLevel: No parameter help available
			- Aggr_Level_4: enums.AggrLevel: No parameter help available
			- Aggr_Level_8: enums.AggrLevel: No parameter help available
			- Aggr_Level_16: enums.AggrLevel: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Aggr_Level_1', enums.AggrLevel),
			ArgStruct.scalar_enum('Aggr_Level_2', enums.AggrLevel),
			ArgStruct.scalar_enum('Aggr_Level_4', enums.AggrLevel),
			ArgStruct.scalar_enum('Aggr_Level_8', enums.AggrLevel),
			ArgStruct.scalar_enum('Aggr_Level_16', enums.AggrLevel)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aggr_Level_1: enums.AggrLevel = None
			self.Aggr_Level_2: enums.AggrLevel = None
			self.Aggr_Level_4: enums.AggrLevel = None
			self.Aggr_Level_8: enums.AggrLevel = None
			self.Aggr_Level_16: enums.AggrLevel = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:IBWP:COReset:NCANdidates \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ibwp.coreset.ncandidates.get(cell_name = 'abc') \n
		Configures the number of PDCCH candidates per aggregation level. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:IBWP:COReset:NCANdidates? {param}', self.__class__.GetStruct())
