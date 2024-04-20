from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbCls:
	"""Rb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rb", core, parent)

	def set(self, cell_name: str, nrb: int, start_rb: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:OCNG:PDCCh:RB \n
		Snippet: driver.configure.signaling.nradio.cell.power.downlink.ocng.pdcch.rb.set(cell_name = 'abc', nrb = 1, start_rb = 1) \n
		No command help available \n
			:param cell_name: No help available
			:param nrb: No help available
			:param start_rb: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('nrb', nrb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:OCNG:PDCCh:RB {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Nrb: int: No parameter help available
			- Start_Rb: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Nrb'),
			ArgStruct.scalar_int('Start_Rb')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Nrb: int = None
			self.Start_Rb: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:OCNG:PDCCh:RB \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.power.downlink.ocng.pdcch.rb.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:OCNG:PDCCh:RB? {param}', self.__class__.GetStruct())
