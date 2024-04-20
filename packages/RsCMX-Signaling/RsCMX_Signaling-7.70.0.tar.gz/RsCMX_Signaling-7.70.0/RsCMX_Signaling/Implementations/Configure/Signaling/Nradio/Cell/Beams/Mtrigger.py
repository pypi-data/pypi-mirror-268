from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MtriggerCls:
	"""Mtrigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtrigger", core, parent)

	def set(self, cell_name: str, trigger: enums.BeamsTrigger) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BEAMs:MTRigger \n
		Snippet: driver.configure.signaling.nradio.cell.beams.mtrigger.set(cell_name = 'abc', trigger = enums.BeamsTrigger.ACTive) \n
		Triggers the P-3 process on the active CSI-RS beam or on a selected CSI-RS beam. \n
			:param cell_name: No help available
			:param trigger: Selects the CSI-RS beam.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('trigger', trigger, DataType.Enum, enums.BeamsTrigger))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BEAMs:MTRigger {param}'.rstrip())
