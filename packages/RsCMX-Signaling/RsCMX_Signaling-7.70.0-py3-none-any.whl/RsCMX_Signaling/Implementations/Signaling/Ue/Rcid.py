from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcidCls:
	"""Rcid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcid", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.RedCapId:
		"""SCPI: FETCh:SIGNaling:UE:RCID \n
		Snippet: value: enums.RedCapId = driver.signaling.ue.rcid.fetch() \n
		Queries the method via which the UE was identified as RedCap UE. \n
			:return: red_cap_id:
				- UNSPecified: UE not identified as RedCap UE
				- PRACh: Identification during the RACH procedure via msg1 (PRACH occasion or PRACH preamble) .
				- MSG3: Identification during the RACH procedure via msg3, containing the logical channel ID (LCID) .
				- UECap: Identification via the UE capability report."""
		response = self._core.io.query_str(f'FETCh:SIGNaling:UE:RCID?')
		return Conversions.str_to_scalar_enum(response, enums.RedCapId)
