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
class PalphaSetCls:
	"""PalphaSet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("palphaSet", core, parent)

	def set(self, cell_name: str, enable: bool, alpha: enums.Alpha = None, p_0: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:PALPhaset \n
		Snippet: driver.configure.signaling.nradio.cell.power.control.palphaSet.set(cell_name = 'abc', enable = False, alpha = enums.Alpha.A00, p_0 = 1) \n
		Sets the parameters 'alpha' and 'p0' of the 'P0-PUSCH-AlphaSet' that is signaled to the UE, for the initial BWP. \n
			:param cell_name: No help available
			:param enable: ON: Signal the 'P0-PUSCH-AlphaSet'. OFF: Do not signal the 'P0-PUSCH-AlphaSet'.
			:param alpha: No help available
			:param p_0: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean), ArgSingle('alpha', alpha, DataType.Enum, enums.Alpha, is_optional=True), ArgSingle('p_0', p_0, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:PALPhaset {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: ON: Signal the 'P0-PUSCH-AlphaSet'. OFF: Do not signal the 'P0-PUSCH-AlphaSet'.
			- Alpha: enums.Alpha: No parameter help available
			- P_0: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_enum('Alpha', enums.Alpha),
			ArgStruct.scalar_int('P_0')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Alpha: enums.Alpha = None
			self.P_0: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:CONTrol:PALPhaset \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.power.control.palphaSet.get(cell_name = 'abc') \n
		Sets the parameters 'alpha' and 'p0' of the 'P0-PUSCH-AlphaSet' that is signaled to the UE, for the initial BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:POWer:CONTrol:PALPhaset? {param}', self.__class__.GetStruct())
