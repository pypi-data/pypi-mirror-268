from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EutraCls:
	"""Eutra commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eutra", core, parent)

	def set_bands(self, fbi: List[int]) -> None:
		"""SCPI: ADD:SIGNaling:EPS:UECapability:EUTRa:BANDs \n
		Snippet: driver.add.signaling.eps.ueCapability.eutra.set_bands(fbi = [1, 2, 3]) \n
		Adds entries to the list of requested frequency bands for the container type 'UE-EUTRA-Capability', for EPS tracking
		areas. \n
			:param fbi: Comma-separated list of LTE frequency band indicators
		"""
		param = Conversions.list_to_csv_str(fbi)
		self._core.io.write(f'ADD:SIGNaling:EPS:UECapability:EUTRa:BANDs {param}')
