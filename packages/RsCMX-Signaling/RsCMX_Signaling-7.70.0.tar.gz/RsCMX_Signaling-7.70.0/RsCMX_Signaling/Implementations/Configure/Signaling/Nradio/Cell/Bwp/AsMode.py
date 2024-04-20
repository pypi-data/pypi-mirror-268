from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AsModeCls:
	"""AsMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asMode", core, parent)

	def set(self, cell_name: str, asn_1_signal_mode: enums.Asn1SignalMode, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwpid>:ASMode \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.asMode.set(cell_name = 'abc', asn_1_signal_mode = enums.Asn1SignalMode.B1, bwParts = repcap.BwParts.Default) \n
		Selects the maximum number of BWPs signaled to the UE. \n
			:param cell_name: No help available
			:param asn_1_signal_mode: Based on UE capability, maximum 1 / 2 / 4 BWPs
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('asn_1_signal_mode', asn_1_signal_mode, DataType.Enum, enums.Asn1SignalMode))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:ASMode {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Asn1SignalMode:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwpid>:ASMode \n
		Snippet: value: enums.Asn1SignalMode = driver.configure.signaling.nradio.cell.bwp.asMode.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the maximum number of BWPs signaled to the UE. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: asn_1_signal_mode: Based on UE capability, maximum 1 / 2 / 4 BWPs"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:ASMode? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Asn1SignalMode)
