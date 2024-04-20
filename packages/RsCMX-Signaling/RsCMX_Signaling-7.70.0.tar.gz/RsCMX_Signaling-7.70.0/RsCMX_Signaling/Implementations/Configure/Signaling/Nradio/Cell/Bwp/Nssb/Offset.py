from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, cell_name: str, time_offset: enums.TimeOffset, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:NSSB:OFFSet \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.nssb.offset.set(cell_name = 'abc', time_offset = enums.TimeOffset.T0, bwParts = repcap.BwParts.Default) \n
		Configures the time offset between the first burst of the NCD-SSB and the first burst of the CD-SSB, signaled as
		'ssb-TimeOffset-r17', for BWP <bb>. \n
			:param cell_name: No help available
			:param time_offset: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('time_offset', time_offset, DataType.Enum, enums.TimeOffset))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:NSSB:OFFSet {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.TimeOffset:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:NSSB:OFFSet \n
		Snippet: value: enums.TimeOffset = driver.configure.signaling.nradio.cell.bwp.nssb.offset.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the time offset between the first burst of the NCD-SSB and the first burst of the CD-SSB, signaled as
		'ssb-TimeOffset-r17', for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: time_offset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:NSSB:OFFSet? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TimeOffset)
