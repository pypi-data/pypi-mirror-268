from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfigCls:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Index: int: Number of the TRS configuration.
			- Bw_Selection: enums.BwSelection: All RBs of the BWP or maximum 52 RBs.
			- Slot_Offset: int: Time domain offset.
			- Symbol_Pair: enums.SymbolPair: Selects the two OFDM symbols used for TRS. The first digit indicates the first symbol. The remaining digits indicate the second symbol. Example: S913 means symbol 9 and symbol 13.
			- Periodicity: enums.TrsPeriodicity: Periodicity for transmission of the resource set, in ms.
			- No_Consec_Slots: int: Number of slots per resource set in FR2."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_int('Index'),
			ArgStruct.scalar_enum('Bw_Selection', enums.BwSelection),
			ArgStruct.scalar_int('Slot_Offset'),
			ArgStruct.scalar_enum('Symbol_Pair', enums.SymbolPair),
			ArgStruct.scalar_enum('Periodicity', enums.TrsPeriodicity),
			ArgStruct.scalar_int('No_Consec_Slots')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Index: int = None
			self.Bw_Selection: enums.BwSelection = None
			self.Slot_Offset: int = None
			self.Symbol_Pair: enums.SymbolPair = None
			self.Periodicity: enums.TrsPeriodicity = None
			self.No_Consec_Slots: int = None

	def set(self, structure: SetStruct, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CSI:TRS:CONFig \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.bwp.csi.trs.config.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Index: int = 1 \n
		structure.Bw_Selection: enums.BwSelection = enums.BwSelection.ALL \n
		structure.Slot_Offset: int = 1 \n
		structure.Symbol_Pair: enums.SymbolPair = enums.SymbolPair.S04 \n
		structure.Periodicity: enums.TrsPeriodicity = enums.TrsPeriodicity.P10 \n
		structure.No_Consec_Slots: int = 1 \n
		driver.configure.signaling.nradio.cell.bwp.csi.trs.config.set(structure, bwParts = repcap.BwParts.Default) \n
		Defines settings of TRS <Index>, for BWP <bb>. If there are several TRS configurations, a query returns the settings of
		all TRS configurations. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CSI:TRS:CONFig', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: int: Number of the TRS configuration.
			- Bw_Selection: enums.BwSelection: All RBs of the BWP or maximum 52 RBs.
			- Slot_Offset: int: Time domain offset.
			- Symbol_Pair: enums.SymbolPair: Selects the two OFDM symbols used for TRS. The first digit indicates the first symbol. The remaining digits indicate the second symbol. Example: S913 means symbol 9 and symbol 13.
			- Periodicity: enums.TrsPeriodicity: Periodicity for transmission of the resource set, in ms.
			- No_Consec_Slots: int: Number of slots per resource set in FR2."""
		__meta_args_list = [
			ArgStruct.scalar_int('Index'),
			ArgStruct.scalar_enum('Bw_Selection', enums.BwSelection),
			ArgStruct.scalar_int('Slot_Offset'),
			ArgStruct.scalar_enum('Symbol_Pair', enums.SymbolPair),
			ArgStruct.scalar_enum('Periodicity', enums.TrsPeriodicity),
			ArgStruct.scalar_int('No_Consec_Slots')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: int = None
			self.Bw_Selection: enums.BwSelection = None
			self.Slot_Offset: int = None
			self.Symbol_Pair: enums.SymbolPair = None
			self.Periodicity: enums.TrsPeriodicity = None
			self.No_Consec_Slots: int = None

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CSI:TRS:CONFig \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.csi.trs.config.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines settings of TRS <Index>, for BWP <bb>. If there are several TRS configurations, a query returns the settings of
		all TRS configurations. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CSI:TRS:CONFig? {param}', self.__class__.GetStruct())
