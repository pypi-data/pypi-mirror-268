from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PalphaSetCls:
	"""PalphaSet commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("palphaSet", core, parent)

	def set(self, cell_name: str, enable: bool, alpha: enums.Alpha = None, p_0: int = None, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:PALPhaset \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.power.control.palphaSet.set(cell_name = 'abc', enable = False, alpha = enums.Alpha.A00, p_0 = 1, bwParts = repcap.BwParts.Default) \n
		Sets the parameters 'alpha' and 'p0' of the 'P0-PUSCH-AlphaSet' that is signaled to the UE, for BWP <bb>. \n
			:param cell_name: No help available
			:param enable: ON: Signal the 'P0-PUSCH-AlphaSet'. OFF: Do not signal the 'P0-PUSCH-AlphaSet'.
			:param alpha: No help available
			:param p_0: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Boolean), ArgSingle('alpha', alpha, DataType.Enum, enums.Alpha, is_optional=True), ArgSingle('p_0', p_0, DataType.Integer, None, is_optional=True))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:PALPhaset {param}'.rstrip())

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

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:PALPhaset \n
		Snippet: value: GetStruct = driver.configure.signaling.nradio.cell.bwp.power.control.palphaSet.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Sets the parameters 'alpha' and 'p0' of the 'P0-PUSCH-AlphaSet' that is signaled to the UE, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:PALPhaset? {param}', self.__class__.GetStruct())
