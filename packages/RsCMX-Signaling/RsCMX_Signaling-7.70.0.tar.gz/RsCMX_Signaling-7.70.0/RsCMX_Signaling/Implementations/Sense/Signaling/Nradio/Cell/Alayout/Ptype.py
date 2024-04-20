from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtypeCls:
	"""Ptype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptype", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PannelType:
		"""SCPI: SENSe:SIGNaling:NRADio:CELL:ALAYout:PTYPe \n
		Snippet: value: enums.PannelType = driver.sense.signaling.nradio.cell.alayout.ptype.get(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
			:return: pannel_type: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'SENSe:SIGNaling:NRADio:CELL:ALAYout:PTYPe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PannelType)
