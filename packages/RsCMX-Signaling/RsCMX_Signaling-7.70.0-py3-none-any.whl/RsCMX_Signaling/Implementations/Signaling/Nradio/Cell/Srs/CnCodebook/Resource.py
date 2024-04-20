from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResourceCls:
	"""Resource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resource", core, parent)

	def delete(self, cell_name: str) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource \n
		Snippet: driver.signaling.nradio.cell.srs.cnCodebook.resource.delete(cell_name = 'abc') \n
		Removes an SRS resource from the resource set for periodic SRS, for the initial BWP. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL:SRS:CNCodebook:RESource {param}')
