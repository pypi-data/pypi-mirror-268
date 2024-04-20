from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NradioCls:
	"""Nradio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nradio", core, parent)

	def get_bands(self) -> List[int]:
		"""SCPI: CATalog:SIGNaling:EPS:UECapability:NRADio:BANDs \n
		Snippet: value: List[int] = driver.catalog.signaling.eps.ueCapability.nradio.get_bands() \n
		Queries the list of requested frequency bands configured for the container type 'UE-NR-Capability', for EPS tracking
		areas. \n
			:return: fbi: Comma-separated list of NR frequency band indicators NAV indicates that there are no requested bands.
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CATalog:SIGNaling:EPS:UECapability:NRADio:BANDs?')
		return response
