from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeTrs, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CSI:TRS:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.csi.trs.mode.set(cell_name = 'abc', mode = enums.ModeTrs.DEF, bwParts = repcap.BwParts.Default) \n
		Selects the configuration mode for TRS transmission, for BWP <bb>. \n
			:param cell_name: No help available
			:param mode: OFF: no TRS DEF: TRS according to 3GPP TS 38.508 UDEF: user-defined TRS
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeTrs))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CSI:TRS:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.ModeTrs:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CSI:TRS:MODE \n
		Snippet: value: enums.ModeTrs = driver.configure.signaling.nradio.cell.bwp.csi.trs.mode.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the configuration mode for TRS transmission, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mode: OFF: no TRS DEF: TRS according to 3GPP TS 38.508 UDEF: user-defined TRS"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CSI:TRS:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeTrs)
