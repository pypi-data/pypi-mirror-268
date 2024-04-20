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

	def set(self, cell_name: str, choice: enums.Choice, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TSCHema:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.pusch.tschema.mode.set(cell_name = 'abc', choice = enums.Choice.CODebook, bwParts = repcap.BwParts.Default) \n
		Selects the PUSCH transmission scheme, signaled as 'txConfig', for BWP <bb>. \n
			:param cell_name: No help available
			:param choice: SINGle: single antenna port, 'txConfig' not signaled CODebook: codebook-based transmission NCODebook: currently not supported
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('choice', choice, DataType.Enum, enums.Choice))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TSCHema:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Choice:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TSCHema:MODE \n
		Snippet: value: enums.Choice = driver.configure.signaling.nradio.cell.bwp.pusch.tschema.mode.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the PUSCH transmission scheme, signaled as 'txConfig', for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: choice: SINGle: single antenna port, 'txConfig' not signaled CODebook: codebook-based transmission NCODebook: currently not supported"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TSCHema:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Choice)
