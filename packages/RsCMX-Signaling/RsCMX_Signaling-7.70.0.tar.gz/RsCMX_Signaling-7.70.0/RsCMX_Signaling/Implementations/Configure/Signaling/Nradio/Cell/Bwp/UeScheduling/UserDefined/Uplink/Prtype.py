from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrtypeCls:
	"""Prtype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prtype", core, parent)

	def set(self, cell_name: str, type_py: enums.Prtype, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:UDEFined:UL:PRTYpe \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.uplink.prtype.set(cell_name = 'abc', type_py = enums.Prtype.OFF, bwParts = repcap.BwParts.Default) \n
		Specifies the PUSCH repetition type signaled as 'pusch-RepTypeIndicatorDCI-0-1', for BWP <bb>. \n
			:param cell_name: No help available
			:param type_py: Not signaled, type A, type B.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('type_py', type_py, DataType.Enum, enums.Prtype))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:UDEFined:UL:PRTYpe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Prtype:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:UDEFined:UL:PRTYpe \n
		Snippet: value: enums.Prtype = driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.uplink.prtype.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Specifies the PUSCH repetition type signaled as 'pusch-RepTypeIndicatorDCI-0-1', for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: type_py: Not signaled, type A, type B."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:UDEFined:UL:PRTYpe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Prtype)
