from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FptModeCls:
	"""FptMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fptMode", core, parent)

	def set(self, cell_name: str, mode: enums.FtpMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:FPTMode \n
		Snippet: driver.configure.signaling.nradio.cell.pusch.tschema.codebook.fptMode.set(cell_name = 'abc', mode = enums.FtpMode.AUTO) \n
		Selects the signaled 'ul-FullPowerTransmission-r16', for the initial BWP. \n
			:param cell_name: No help available
			:param mode: AUTO: signaled value selected via reported UE capabilities FULL: signaled value 'fullpower' MOD1: signaled value 'fullpowerMode1' MOD2: signaled value 'fullpowerMode2' OFF: 'ul-FullPowerTransmission-r16' not signaled
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.FtpMode))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:FPTMode {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.FtpMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:FPTMode \n
		Snippet: value: enums.FtpMode = driver.configure.signaling.nradio.cell.pusch.tschema.codebook.fptMode.get(cell_name = 'abc') \n
		Selects the signaled 'ul-FullPowerTransmission-r16', for the initial BWP. \n
			:param cell_name: No help available
			:return: mode: AUTO: signaled value selected via reported UE capabilities FULL: signaled value 'fullpower' MOD1: signaled value 'fullpowerMode1' MOD2: signaled value 'fullpowerMode2' OFF: 'ul-FullPowerTransmission-r16' not signaled"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUSCh:TSCHema:CODebook:FPTMode? {param}')
		return Conversions.str_to_scalar_enum(response, enums.FtpMode)
