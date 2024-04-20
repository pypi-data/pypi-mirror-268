from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsTableCls:
	"""McsTable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsTable", core, parent)

	def set(self, cell_name: str, mcs_table: enums.McsTableC, predefined_3_gpp: enums.ConfigTypeB = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCSTable \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.cmMapping.mcsTable.set(cell_name = 'abc', mcs_table = enums.McsTableC.AUTO, predefined_3_gpp = enums.ConfigTypeB.T1) \n
		Selects a configuration mode for the CQI-MCS mapping table for follow WB CQI, for the initial BWP. \n
			:param cell_name: No help available
			:param mcs_table:
				- AUTO: The mapping table is selected automatically, depending on [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:DL:MCSTable.
				- P521: The mapping table contents are defined by 3GPP TS 38.521-4.Table selection via Predefined3GPP.
				- UDEFined: The mapping table contents are defined via a separate command, see [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCS.
			:param predefined_3_gpp: Selects a mapping table for MCSTable = P521. T1: table A.4-1 in 3GPP TS 38.521-4 T2: table A.
			4-2 in 3GPP TS 38.521-4 T3: table A.4-3 in 3GPP TS 38.521-4"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mcs_table', mcs_table, DataType.Enum, enums.McsTableC), ArgSingle('predefined_3_gpp', predefined_3_gpp, DataType.Enum, enums.ConfigTypeB, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCSTable {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Mcs_Table: enums.McsTableC:
				- AUTO: The mapping table is selected automatically, depending on [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:UDEFined:DL:MCSTable.
				- P521: The mapping table contents are defined by 3GPP TS 38.521-4.Table selection via Predefined3GPP.
				- UDEFined: The mapping table contents are defined via a separate command, see [CONFigure:]SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCS.
			- Predefined_3_Gpp: enums.ConfigTypeB: Selects a mapping table for MCSTable = P521. T1: table A.4-1 in 3GPP TS 38.
			521-4 T2: table A.4-2 in 3GPP TS 38.521-4 T3: table A.4-3 in 3GPP TS 38.521-4"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mcs_Table', enums.McsTableC),
			ArgStruct.scalar_enum('Predefined_3_Gpp', enums.ConfigTypeB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mcs_Table: enums.McsTableC = None
			self.Predefined_3_Gpp: enums.ConfigTypeB = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCSTable \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ueScheduling.cmMapping.mcsTable.get(cell_name = 'abc') \n
		Selects a configuration mode for the CQI-MCS mapping table for follow WB CQI, for the initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:CMMapping:MCSTable? {param}', self.__class__.GetStruct())
