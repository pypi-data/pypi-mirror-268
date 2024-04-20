from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MrdcCls:
	"""Mrdc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mrdc", core, parent)

	# noinspection PyTypeChecker
	class BandsStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Rat: List[enums.CellType]: Type of the band: LTE band or NR band.
			- Fbi: List[int]: Frequency band indicator"""
		__meta_args_list = [
			ArgStruct('Rat', DataType.EnumList, enums.CellType, False, True, 1),
			ArgStruct('Fbi', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rat: List[enums.CellType] = None
			self.Fbi: List[int] = None

	def get_bands(self) -> BandsStruct:
		"""SCPI: CATalog:SIGNaling:EPS:UECapability:MRDC:BANDs \n
		Snippet: value: BandsStruct = driver.catalog.signaling.eps.ueCapability.mrdc.get_bands() \n
		Queries the list of requested frequency bands configured for the container type 'UE-MRDC-Capability', for EPS tracking
		areas. The bands are returned as pairs of values: {<Rat>, <Fbi>}1, {<Rat>, <Fbi>}2, ... A returned pair of NAV indicates
		that there are no requested bands. \n
			:return: structure: for return value, see the help for BandsStruct structure arguments.
		"""
		return self._core.io.query_struct('CATalog:SIGNaling:EPS:UECapability:MRDC:BANDs?', self.__class__.BandsStruct())
