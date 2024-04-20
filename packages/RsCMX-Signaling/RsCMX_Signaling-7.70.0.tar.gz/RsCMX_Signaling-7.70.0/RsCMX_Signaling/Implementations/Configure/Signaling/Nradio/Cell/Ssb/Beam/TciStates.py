from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TciStatesCls:
	"""TciStates commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tciStates", core, parent)

	def set_update(self, cell_name: str) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:SSB:BEAM:TCIStates:UPDate \n
		Snippet: driver.configure.signaling.nradio.cell.ssb.beam.tciStates.set_update(cell_name = 'abc') \n
		Updates transmission configuration indicator (TCI) states. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:SSB:BEAM:TCIStates:UPDate {param}')
