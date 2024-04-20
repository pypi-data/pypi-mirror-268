from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InactiveCls:
	"""Inactive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inactive", core, parent)

	def set(self, ue_id: str = None, rnau_timer: enums.RnauTimer = None, paging_cycle: enums.PagingCycle = None) -> None:
		"""SCPI: PROCedure:SIGNaling:UE:RRC:INACtive \n
		Snippet: driver.procedure.signaling.ue.rrc.inactive.set(ue_id = 'abc', rnau_timer = enums.RnauTimer.M10, paging_cycle = enums.PagingCycle.P128) \n
		Suspends a 5G NR standalone RRC connection (RRC release with 'suspendConfig') , resulting in the RRC state Inactive. \n
			:param ue_id: No help available
			:param rnau_timer: RNAU timer triggering the periodic RAN-based notification area update, in minutes
			:param paging_cycle: UE-specific cycle for RAN-initiated paging, as number of radio frames
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ue_id', ue_id, DataType.String, None, is_optional=True), ArgSingle('rnau_timer', rnau_timer, DataType.Enum, enums.RnauTimer, is_optional=True), ArgSingle('paging_cycle', paging_cycle, DataType.Enum, enums.PagingCycle, is_optional=True))
		self._core.io.write(f'PROCedure:SIGNaling:UE:RRC:INACtive {param}'.rstrip())
