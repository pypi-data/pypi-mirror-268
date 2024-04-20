from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfrequencyCls:
	"""Cfrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfrequency", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Dl_Frequency: float: DL carrier center frequency
			- Ul_Frequency: float: UL carrier center frequency"""
		__meta_args_list = [
			ArgStruct.scalar_float('Dl_Frequency'),
			ArgStruct.scalar_float('Ul_Frequency')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dl_Frequency: float = None
			self.Ul_Frequency: float = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:RFSettings:CFRequency \n
		Snippet: value: GetStruct = driver.sense.signaling.nradio.cell.rfSettings.cfrequency.get(cell_name = 'abc') \n
		Queries the carrier center frequencies. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'SENSe:SIGNaling:NRADio:CELL:RFSettings:CFRequency? {param}', self.__class__.GetStruct())
