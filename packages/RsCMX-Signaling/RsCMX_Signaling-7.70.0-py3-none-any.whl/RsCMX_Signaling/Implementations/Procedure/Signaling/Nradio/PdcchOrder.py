from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchOrderCls:
	"""PdcchOrder commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcchOrder", core, parent)

	def activate(self, mode: enums.ConfigMode = None, ra_preamble_idx: int = None, ssb_index: int = None, prach_mask_index: int = None) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:PDCChorder:ACTivate \n
		Snippet: driver.procedure.signaling.nradio.pdcchOrder.activate(mode = enums.ConfigMode.AUTO, ra_preamble_idx = 1, ssb_index = 1, prach_mask_index = 1) \n
		Triggers a PDCCH order for the primary NR cell (established connection needed) . \n
			:param mode: AUTO: Automatic configuration, ignore the remaining parameters. UDEFined: Configuration via the remaining parameters.
			:param ra_preamble_idx: Random access preamble index
			:param ssb_index: SS/PBCH index
			:param prach_mask_index: PRACH mask index
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mode', mode, DataType.Enum, enums.ConfigMode, is_optional=True), ArgSingle('ra_preamble_idx', ra_preamble_idx, DataType.Integer, None, is_optional=True), ArgSingle('ssb_index', ssb_index, DataType.Integer, None, is_optional=True), ArgSingle('prach_mask_index', prach_mask_index, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:PDCChorder:ACTivate {param}'.rstrip())
