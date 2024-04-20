from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CnCodebookCls:
	"""CnCodebook commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cnCodebook", core, parent)

	def set_resource(self, cell_name: str) -> None:
		"""SCPI: ADD:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource \n
		Snippet: driver.add.signaling.nradio.cell.srs.cnCodebook.set_resource(cell_name = 'abc') \n
		Adds an SRS resource to the resource set for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'ADD:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource {param}')
