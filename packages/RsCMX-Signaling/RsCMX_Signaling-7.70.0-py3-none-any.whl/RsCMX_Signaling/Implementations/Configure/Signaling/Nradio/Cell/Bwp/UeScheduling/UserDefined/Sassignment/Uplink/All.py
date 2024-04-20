from typing import List

from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.StructBase import StructBase
from ...........Internal.ArgStruct import ArgStruct
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Slot: List[int]: Index number of the slot
			- Enable: List[bool]: No parameter help available
			- Number_Rb: List[int]: No parameter help available
			- Start_Rb: List[int]: No parameter help available
			- Mcs: List[int]: No parameter help available
			- Dci_Format: List[enums.DciFormatC]: No parameter help available
			- Mimo: List[enums.MimoB]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct('Slot', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Number_Rb', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Start_Rb', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mcs', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dci_Format', DataType.EnumList, enums.DciFormatC, False, True, 1),
			ArgStruct('Mimo', DataType.EnumList, enums.MimoB, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Slot: List[int] = None
			self.Enable: List[bool] = None
			self.Number_Rb: List[int] = None
			self.Start_Rb: List[int] = None
			self.Mcs: List[int] = None
			self.Dci_Format: List[enums.DciFormatC] = None
			self.Mimo: List[enums.MimoB] = None

	def set(self, structure: SetStruct, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:UDEFined:SASSignment:UL:ALL \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.sassignment.uplink.all.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Slot: List[int] = [1, 2, 3] \n
		structure.Enable: List[bool] = [True, False, True] \n
		structure.Number_Rb: List[int] = [1, 2, 3] \n
		structure.Start_Rb: List[int] = [1, 2, 3] \n
		structure.Mcs: List[int] = [1, 2, 3] \n
		structure.Dci_Format: List[enums.DciFormatC] = [DciFormatC.D00, DciFormatC.D01] \n
		structure.Mimo: List[enums.MimoB] = [MimoB.M22, MimoB.SISO] \n
		driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.sassignment.uplink.all.set(structure, bwParts = repcap.BwParts.Default) \n
		Defines scheduling settings for one or more UL slots, for BWP <bb>. The parameter sequence contains one set of values per
		slot: <CellName>, {<Slot>, <Enable>, <NumberRB>, <StartRB>, <MCS>, <DCIFormat>, <Mimo>}slot a, {...}slot b, ... A query
		returns all UL slots. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:UDEFined:SASSignment:UL:ALL', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Slot: List[int]: Index number of the slot
			- Enable: List[bool]: No parameter help available
			- Number_Rb: List[int]: No parameter help available
			- Start_Rb: List[int]: No parameter help available
			- Mcs: List[int]: No parameter help available
			- Dci_Format: List[enums.DciFormatC]: No parameter help available
			- Mimo: List[enums.MimoB]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Slot', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Number_Rb', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Start_Rb', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Mcs', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dci_Format', DataType.EnumList, enums.DciFormatC, False, True, 1),
			ArgStruct('Mimo', DataType.EnumList, enums.MimoB, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Slot: List[int] = None
			self.Enable: List[bool] = None
			self.Number_Rb: List[int] = None
			self.Start_Rb: List[int] = None
			self.Mcs: List[int] = None
			self.Dci_Format: List[enums.DciFormatC] = None
			self.Mimo: List[enums.MimoB] = None

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:UDEFined:SASSignment:UL:ALL \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.sassignment.uplink.all.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines scheduling settings for one or more UL slots, for BWP <bb>. The parameter sequence contains one set of values per
		slot: <CellName>, {<Slot>, <Enable>, <NumberRB>, <StartRB>, <MCS>, <DCIFormat>, <Mimo>}slot a, {...}slot b, ... A query
		returns all UL slots. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:UDEFined:SASSignment:UL:ALL? {param}', self.__class__.GetStruct())
