from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FptModeCls:
	"""FptMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fptMode", core, parent)

	def set(self, cell_name: str, mode: enums.FtpMode, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TSCHema:CODebook:FPTMode \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.pusch.tschema.codebook.fptMode.set(cell_name = 'abc', mode = enums.FtpMode.AUTO, bwParts = repcap.BwParts.Default) \n
		Selects the signaled 'ul-FullPowerTransmission-r16', for BWP <bb>. \n
			:param cell_name: No help available
			:param mode: AUTO: signaled value selected via reported UE capabilities FULL: signaled value 'fullpower' MOD1: signaled value 'fullpowerMode1' MOD2: signaled value 'fullpowerMode2' OFF: 'ul-FullPowerTransmission-r16' not signaled
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.FtpMode))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TSCHema:CODebook:FPTMode {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.FtpMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUSCh:TSCHema:CODebook:FPTMode \n
		Snippet: value: enums.FtpMode = driver.configure.signaling.nradio.cell.bwp.pusch.tschema.codebook.fptMode.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the signaled 'ul-FullPowerTransmission-r16', for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mode: AUTO: signaled value selected via reported UE capabilities FULL: signaled value 'fullpower' MOD1: signaled value 'fullpowerMode1' MOD2: signaled value 'fullpowerMode2' OFF: 'ul-FullPowerTransmission-r16' not signaled"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUSCh:TSCHema:CODebook:FPTMode? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FtpMode)
