from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqErrorCls:
	"""FreqError commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("freqError", core, parent)

	def set(self, cell_name: str, frequency_error: float) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:DL:FERRor \n
		Snippet: driver.configure.signaling.lte.cell.rfSettings.downlink.freqError.set(cell_name = 'abc', frequency_error = 1.0) \n
		Configures a frequency error to be added to the configured DL carrier center frequency. \n
			:param cell_name: No help available
			:param frequency_error: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('frequency_error', frequency_error, DataType.Float))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:DL:FERRor {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency_Error: float: No parameter help available
			- Res_Center_Freq: int: Center frequency resulting from nominal center frequency plus frequency error."""
		__meta_args_list = [
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_int('Res_Center_Freq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency_Error: float = None
			self.Res_Center_Freq: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:RFSettings:DL:FERRor \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.rfSettings.downlink.freqError.get(cell_name = 'abc') \n
		Configures a frequency error to be added to the configured DL carrier center frequency. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:RFSettings:DL:FERRor? {param}', self.__class__.GetStruct())
