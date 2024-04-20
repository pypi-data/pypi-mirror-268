from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FhoppingCls:
	"""Fhopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhopping", core, parent)

	def set(self, cell_name: str, csrs: int, bsrs: int = None, bhop: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:FHOPping \n
		Snippet: driver.configure.signaling.nradio.cell.srs.fhopping.set(cell_name = 'abc', csrs = 1, bsrs = 1, bhop = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param csrs: No help available
			:param bsrs: No help available
			:param bhop: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('csrs', csrs, DataType.Integer), ArgSingle('bsrs', bsrs, DataType.Integer, None, is_optional=True), ArgSingle('bhop', bhop, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SRS:FHOPping {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Csrs: int: No parameter help available
			- Bsrs: int: No parameter help available
			- Bhop: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Csrs'),
			ArgStruct.scalar_int('Bsrs'),
			ArgStruct.scalar_int('Bhop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Csrs: int = None
			self.Bsrs: int = None
			self.Bhop: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SRS:FHOPping \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.srs.fhopping.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:SRS:FHOPping? {param}', self.__class__.GetStruct())
