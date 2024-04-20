from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsTableCls:
	"""McsTable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsTable", core, parent)

	def set(self, cell_name: str, mcs_table: enums.McsTableC, predefined_3_gpp: enums.Predefined3Gpp = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCSTable \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.cmMapping.csirs.mcsTable.set(cell_name = 'abc', mcs_table = enums.McsTableC.AUTO, predefined_3_gpp = enums.Predefined3Gpp.M1) \n
		Selects a configuration mode for the CQI-MCS mapping tables for follow WB CQI. There is a mapping table for each type of
		DL subframe: CSI-RS subframe (CSIRs) , special subframe for TDD (SSUBframe) , all other subframes (NSUBframe) . \n
			:param cell_name: No help available
			:param mcs_table:
				- AUTO: Mapping table selected automatically, depending on [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:MCSTable.
				- P521: Mapping table contents defined by 3GPP TS 36.521.MCS scheme selection via Predefined3GPP.
				- UDEFined: Mapping table contents defined via separate command, see [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCS etc.
			:param predefined_3_gpp: Selects an MCS scheme for MCSTable = P521. Mn means 'MCS.n' in the tables A.4-13 to A.4-16 in
			3GPP TS 36.521."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs_table', mcs_table, DataType.Enum, enums.McsTableC), ArgSingle('predefined_3_gpp', predefined_3_gpp, DataType.Enum, enums.Predefined3Gpp, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCSTable {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Mcs_Table: enums.McsTableC:
				- AUTO: Mapping table selected automatically, depending on [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:UDEFined:SASSignment:DL:MCSTable.
				- P521: Mapping table contents defined by 3GPP TS 36.521.MCS scheme selection via Predefined3GPP.
				- UDEFined: Mapping table contents defined via separate command, see [CONFigure:]SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCS etc.
			- Predefined_3_Gpp: enums.Predefined3Gpp: Selects an MCS scheme for MCSTable = P521. Mn means 'MCS.n' in the tables A.
			4-13 to A.4-16 in 3GPP TS 36.521."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mcs_Table', enums.McsTableC),
			ArgStruct.scalar_enum('Predefined_3_Gpp', enums.Predefined3Gpp)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcs_Table: enums.McsTableC = None
			self.Predefined_3_Gpp: enums.Predefined3Gpp = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCSTable \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.ueScheduling.cmMapping.csirs.mcsTable.get(cell_name = 'abc') \n
		Selects a configuration mode for the CQI-MCS mapping tables for follow WB CQI. There is a mapping table for each type of
		DL subframe: CSI-RS subframe (CSIRs) , special subframe for TDD (SSUBframe) , all other subframes (NSUBframe) . \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:CMMapping:CSIRs:MCSTable? {param}', self.__class__.GetStruct())
