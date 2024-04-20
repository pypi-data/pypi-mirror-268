from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandsCls:
	"""Bands commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bands", core, parent)

	def delete(self, rat: List[enums.CellType], fbi: List[int]) -> None:
		"""SCPI: DELete:SIGNaling:EPS:UECapability:MRDC:BANDs \n
		Snippet: driver.signaling.eps.ueCapability.mrdc.bands.delete(rat = [CellType.LTE, CellType.NR], fbi = [1, 2, 3]) \n
		Deletes entries from the list of requested frequency bands for the container type 'UE-MRDC-Capability', for EPS tracking
		areas. The bands are defined as pairs of values: {<Rat>, <Fbi>}1, {<Rat>, <Fbi>}2, ... \n
			:param rat: Type of the band: LTE band or NR band.
			:param fbi: Frequency band indicator
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('rat', rat, DataType.EnumList, enums.CellType), ArgSingle.as_open_list('fbi', fbi, DataType.IntegerList, None))
		self._core.io.write(f'DELete:SIGNaling:EPS:UECapability:MRDC:BANDs {param}'.rstrip())
