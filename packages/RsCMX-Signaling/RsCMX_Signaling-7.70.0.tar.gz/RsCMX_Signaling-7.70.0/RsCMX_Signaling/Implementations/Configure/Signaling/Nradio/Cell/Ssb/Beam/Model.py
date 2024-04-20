from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModelCls:
	"""Model commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("model", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Cell_Name: str: No parameter help available
			- Position: List[int]: Position index (0 to n) in the 'ssb-PositionsInBurst' bitmap.
			- Enable: List[bool]: Use the position for SSB transmission (ON) or not (OFF) .
			- Aoa: List[enums.Aoa]: Optional setting parameter. Angle of arrival for the position. CONDucted: conducted test setup AOA1: Over-the-air test setup, first angle of arrival used AOA2: Over-the-air test setup, second angle of arrival used
			- Phase: List[float]: Optional setting parameter. Phase for the position.
			- Attenuation: List[float]: Optional setting parameter. Power difference for the position."""
		__meta_args_list = [
			ArgStruct.scalar_str('Cell_Name'),
			ArgStruct('Position', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Aoa', DataType.EnumList, enums.Aoa, True, True, 1),
			ArgStruct('Phase', DataType.FloatList, None, True, True, 1),
			ArgStruct('Attenuation', DataType.FloatList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cell_Name: str = None
			self.Position: List[int] = None
			self.Enable: List[bool] = None
			self.Aoa: List[enums.Aoa] = None
			self.Phase: List[float] = None
			self.Attenuation: List[float] = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:BEAM:MODel \n
		Snippet with structure: \n
		structure = driver.configure.signaling.nradio.cell.ssb.beam.model.SetStruct() \n
		structure.Cell_Name: str = 'abc' \n
		structure.Position: List[int] = [1, 2, 3] \n
		structure.Enable: List[bool] = [True, False, True] \n
		structure.Aoa: List[enums.Aoa] = [Aoa.AOA1, Aoa.CONDucted] \n
		structure.Phase: List[float] = [1.1, 2.2, 3.3] \n
		structure.Attenuation: List[float] = [1.1, 2.2, 3.3] \n
		driver.configure.signaling.nradio.cell.ssb.beam.model.set(structure) \n
		Configures the SS-block positions in an SSB burst and the beam properties for each position. Configuration is only
		possible for the mode UDEFined, selected via [CONFigure:]SIGNaling:NRADio:CELL:SSB:BEAM:PIBurst. For other modes, you can
		only query the automatically configured settings. You can configure several positions via one command: <CellName>,
		{<Position>, <Enable>, <AoA>, <Phase>, <Attenuation>}pos a, {...}pos b, ... \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:SIGNaling:NRADio:CELL:SSB:BEAM:MODel', structure)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Position: List[int]: Position index (0 to n) in the 'ssb-PositionsInBurst' bitmap.
			- Enable: List[bool]: Use the position for SSB transmission (ON) or not (OFF) .
			- Aoa: List[enums.Aoa]: Angle of arrival for the position. CONDucted: conducted test setup AOA1: Over-the-air test setup, first angle of arrival used AOA2: Over-the-air test setup, second angle of arrival used
			- Phase: List[float]: Phase for the position.
			- Attenuation: List[float]: Power difference for the position."""
		__meta_args_list = [
			ArgStruct('Position', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Aoa', DataType.EnumList, enums.Aoa, False, True, 1),
			ArgStruct('Phase', DataType.FloatList, None, False, True, 1),
			ArgStruct('Attenuation', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Position: List[int] = None
			self.Enable: List[bool] = None
			self.Aoa: List[enums.Aoa] = None
			self.Phase: List[float] = None
			self.Attenuation: List[float] = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:BEAM:MODel \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.ssb.beam.model.get(cell_name = 'abc') \n
		Configures the SS-block positions in an SSB burst and the beam properties for each position. Configuration is only
		possible for the mode UDEFined, selected via [CONFigure:]SIGNaling:NRADio:CELL:SSB:BEAM:PIBurst. For other modes, you can
		only query the automatically configured settings. You can configure several positions via one command: <CellName>,
		{<Position>, <Enable>, <AoA>, <Phase>, <Attenuation>}pos a, {...}pos b, ... \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:SSB:BEAM:MODel? {param}', self.__class__.GetStruct())
