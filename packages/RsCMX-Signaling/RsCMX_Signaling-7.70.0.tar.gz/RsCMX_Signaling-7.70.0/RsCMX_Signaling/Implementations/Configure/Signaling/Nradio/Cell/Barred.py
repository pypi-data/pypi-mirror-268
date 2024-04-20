from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BarredCls:
	"""Barred commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("barred", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Enable: bool: ON: cell barred OFF: cell not barred
			- Ifri_Present: bool: Optional setting parameter. 'intraFreqReselectionRedCap-r17' = 'allowed'
			- One_Rx_Barred: bool: Optional setting parameter. 'cellBarredRedCap1Rx-r17' = 'barred'
			- Two_Rx_Barred: bool: Optional setting parameter. 'cellBarredRedCap2Rx-r17' = 'barred'
			- Half_Duplex: bool: Optional setting parameter. 'halfDuplexRedCapAllowed-r17' = 'false'"""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_bool_optional('Ifri_Present'),
			ArgStruct.scalar_bool_optional('One_Rx_Barred'),
			ArgStruct.scalar_bool_optional('Two_Rx_Barred'),
			ArgStruct.scalar_bool_optional('Half_Duplex')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Enable: bool = None
			self.Ifri_Present: bool = None
			self.One_Rx_Barred: bool = None
			self.Two_Rx_Barred: bool = None
			self.Half_Duplex: bool = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BARRed \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.barred.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Enable: bool = False \n
		structure.Ifri_Present: bool = False \n
		structure.One_Rx_Barred: bool = False \n
		structure.Two_Rx_Barred: bool = False \n
		structure.Half_Duplex: bool = False \n
		driver.configure.signaling.nradio.cell.barred.set(structure) \n
		Specifies whether the cell is barred. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:BARRed', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: ON: cell barred OFF: cell not barred
			- Ifri_Present: bool: 'intraFreqReselectionRedCap-r17' = 'allowed'
			- One_Rx_Barred: bool: 'cellBarredRedCap1Rx-r17' = 'barred'
			- Two_Rx_Barred: bool: 'cellBarredRedCap2Rx-r17' = 'barred'
			- Half_Duplex: bool: 'halfDuplexRedCapAllowed-r17' = 'false'"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_bool('Ifri_Present'),
			ArgStruct.scalar_bool('One_Rx_Barred'),
			ArgStruct.scalar_bool('Two_Rx_Barred'),
			ArgStruct.scalar_bool('Half_Duplex')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Ifri_Present: bool = None
			self.One_Rx_Barred: bool = None
			self.Two_Rx_Barred: bool = None
			self.Half_Duplex: bool = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BARRed \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.barred.get(cell_name = 'abc') \n
		Specifies whether the cell is barred. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BARRed? {param}', self.__class__.GetStruct())
