from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, cell_name: str, offset: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:RESource:OFFSet \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.cqiReporting.resource.offset.set(cell_name = 'abc', offset = 1, bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param offset: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('offset', offset, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:RESource:OFFSet {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> int:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:CQIReporting:RESource:OFFSet \n
		Snippet: value: int = driver.configure.signaling.nradio.cell.bwp.cqiReporting.resource.offset.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		No command help available \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: offset: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CQIReporting:RESource:OFFSet? {param}')
		return Conversions.str_to_int(response)
