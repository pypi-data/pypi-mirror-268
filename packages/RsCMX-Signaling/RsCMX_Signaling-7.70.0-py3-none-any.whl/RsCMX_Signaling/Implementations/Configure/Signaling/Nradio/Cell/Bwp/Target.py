from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TargetCls:
	"""Target commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("target", core, parent)

	def set(self, cell_name: str, active_dl_bwp: int, active_ul_bwp: int = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP:TARGet \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.target.set(cell_name = 'abc', active_dl_bwp = 1, active_ul_bwp = 1) \n
		Switches the active BWP. \n
			:param cell_name: No help available
			:param active_dl_bwp: Selects the target DL BWP. IBWP: initial BWP integer: BWP ID
			:param active_ul_bwp: Selects the target UL BWP. IBWP: initial BWP integer: BWP ID SADL: same as DL
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('active_dl_bwp', active_dl_bwp, DataType.Integer), ArgSingle('active_ul_bwp', active_ul_bwp, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP:TARGet {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Active_Dl_Bwp: int: Selects the target DL BWP. IBWP: initial BWP integer: BWP ID
			- Active_Ul_Bwp: int: Selects the target UL BWP. IBWP: initial BWP integer: BWP ID SADL: same as DL"""
		__meta_args_list = [
			ArgStruct.scalar_int('Active_Dl_Bwp'),
			ArgStruct.scalar_int('Active_Ul_Bwp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Active_Dl_Bwp: int = None
			self.Active_Ul_Bwp: int = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP:TARGet \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.target.get(cell_name = 'abc') \n
		Switches the active BWP. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP:TARGet? {param}', self.__class__.GetStruct())
