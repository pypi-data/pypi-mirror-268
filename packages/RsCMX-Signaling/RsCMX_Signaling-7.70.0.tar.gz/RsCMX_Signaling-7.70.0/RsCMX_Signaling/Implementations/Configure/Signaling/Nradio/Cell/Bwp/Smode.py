from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmodeCls:
	"""Smode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smode", core, parent)

	def set(self, cell_name: str, switching_mode: enums.BwpSwitchingMode) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP:SMODe \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.smode.set(cell_name = 'abc', switching_mode = enums.BwpSwitchingMode.DYNamic) \n
		Selects a mechanism for sending BWP switching information to the UE. \n
			:param cell_name: No help available
			:param switching_mode:
				- STATic: The BWP is switched via an RRC connection reconfiguration.
				- DYNamic: The BWP is switched by sending a BWP ID in DCI format 0_1 for the UL or format 1_1 for the DL."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('switching_mode', switching_mode, DataType.Enum, enums.BwpSwitchingMode))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP:SMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.BwpSwitchingMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP:SMODe \n
		Snippet: value: enums.BwpSwitchingMode = driver.configure.signaling.nradio.cell.bwp.smode.get(cell_name = 'abc') \n
		Selects a mechanism for sending BWP switching information to the UE. \n
			:param cell_name: No help available
			:return: switching_mode:
				- STATic: The BWP is switched via an RRC connection reconfiguration.
				- DYNamic: The BWP is switched by sending a BWP ID in DCI format 0_1 for the UL or format 1_1 for the DL."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP:SMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.BwpSwitchingMode)
