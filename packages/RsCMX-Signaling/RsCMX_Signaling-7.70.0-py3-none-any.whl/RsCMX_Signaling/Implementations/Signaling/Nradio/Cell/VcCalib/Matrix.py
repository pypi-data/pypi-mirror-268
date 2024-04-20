from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MatrixCls:
	"""Matrix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("matrix", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- G_11_Real: float: No parameter help available
			- G_11_Imaginary: float: No parameter help available
			- G_12_Real: float: No parameter help available
			- G_12_Imaginary: float: No parameter help available
			- G_21_Real: float: No parameter help available
			- G_21_Imaginary: float: No parameter help available
			- G_22_Real: float: No parameter help available
			- G_22_Imaginary: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('G_11_Real'),
			ArgStruct.scalar_float('G_11_Imaginary'),
			ArgStruct.scalar_float('G_12_Real'),
			ArgStruct.scalar_float('G_12_Imaginary'),
			ArgStruct.scalar_float('G_21_Real'),
			ArgStruct.scalar_float('G_21_Imaginary'),
			ArgStruct.scalar_float('G_22_Real'),
			ArgStruct.scalar_float('G_22_Imaginary')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.G_11_Real: float = None
			self.G_11_Imaginary: float = None
			self.G_12_Real: float = None
			self.G_12_Imaginary: float = None
			self.G_21_Real: float = None
			self.G_21_Imaginary: float = None
			self.G_22_Real: float = None
			self.G_22_Imaginary: float = None

	def fetch(self, cell_name: str) -> FetchStruct:
		"""SCPI: FETCh:SIGNaling:NRADio:CELL:VCCalib:MATRix \n
		Snippet: value: FetchStruct = driver.signaling.nradio.cell.vcCalib.matrix.fetch(cell_name = 'abc') \n
		Queries the coefficients of the calibration matrix. There are four coefficients (g11, g12, g21, g22) . Each has a real
		part and an imaginary part. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'FETCh:SIGNaling:NRADio:CELL:VCCalib:MATRix? {param}', self.__class__.FetchStruct())
