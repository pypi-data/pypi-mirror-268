from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandsCls:
	"""Bands commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bands", core, parent)

	def delete(self, fbi: List[int]) -> None:
		"""SCPI: DELete:SIGNaling:EPS:UECapability:NRADio:BANDs \n
		Snippet: driver.signaling.eps.ueCapability.nradio.bands.delete(fbi = [1, 2, 3]) \n
		Deletes entries from the list of requested frequency bands for the container type 'UE-NR-Capability', for EPS tracking
		areas. \n
			:param fbi: Comma-separated list of NR frequency band indicators
		"""
		param = Conversions.list_to_csv_str(fbi)
		self._core.io.write(f'DELete:SIGNaling:EPS:UECapability:NRADio:BANDs {param}')
