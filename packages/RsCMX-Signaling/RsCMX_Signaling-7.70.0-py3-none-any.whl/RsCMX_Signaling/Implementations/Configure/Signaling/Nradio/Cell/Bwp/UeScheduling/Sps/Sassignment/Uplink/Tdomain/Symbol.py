from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.Types import DataType
from ............Internal.StructBase import StructBase
from ............Internal.ArgStruct import ArgStruct
from ............Internal.ArgSingleList import ArgSingleList
from ............Internal.ArgSingle import ArgSingle
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolCls:
	"""Symbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbol", core, parent)

	def set(self, cell_name: str, start_symbol: int, number_symbol: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:SASSignment:UL:TDOMain:SYMBol \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.sassignment.uplink.tdomain.symbol.set(cell_name = 'abc', start_symbol = 1, number_symbol = 1, bwParts = repcap.BwParts.Default) \n
		Defines the index of the first allocated OFDM symbol and the number of allocated OFDM symbols, for UL configured grant,
		for BWP <bb>. \n
			:param cell_name: No help available
			:param start_symbol: No help available
			:param number_symbol: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('start_symbol', start_symbol, DataType.Integer), ArgSingle('number_symbol', number_symbol, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:SASSignment:UL:TDOMain:SYMBol {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Start_Symbol: int: No parameter help available
			- Number_Symbol: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Symbol'),
			ArgStruct.scalar_int('Number_Symbol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Symbol: int = None
			self.Number_Symbol: int = None

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:SASSignment:UL:TDOMain:SYMBol \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.sassignment.uplink.tdomain.symbol.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines the index of the first allocated OFDM symbol and the number of allocated OFDM symbols, for UL configured grant,
		for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:SASSignment:UL:TDOMain:SYMBol? {param}', self.__class__.GetStruct())
