from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
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

	def set(self, cell_name: str, index: int, nrb: int, start_rb: int) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:RB \n
		Snippet: driver.configure.signaling.nradio.cell.harq.uplink.user.retransm.rb.set(cell_name = 'abc', index = 1, nrb = 1, start_rb = 1) \n
		Configures the number of RB and start RB for a certain retransmission, for user-defined UL HARQ, for the initial BWP.
		Only relevant for disabled auto RIV. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param nrb: No help available
			:param start_rb: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('nrb', nrb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:RB {param}'.rstrip())

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

	def get(self, cell_name: str, index: int) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:RB \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.harq.uplink.user.retransm.rb.get(cell_name = 'abc', index = 1) \n
		Configures the number of RB and start RB for a certain retransmission, for user-defined UL HARQ, for the initial BWP.
		Only relevant for disabled auto RIV. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:HARQ:UL:USER:RETRansm:RB? {param}'.rstrip(), self.__class__.GetStruct())
