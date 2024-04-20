from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SprbCls:
	"""Sprb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sprb", core, parent)

	def set(self, cell_name: str, starting_prb: enums.LowHigh, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUCCh:SPRB \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.pucch.sprb.set(cell_name = 'abc', starting_prb = enums.LowHigh.HIGH, bwParts = repcap.BwParts.Default) \n
		Selects the position of the resource blocks: lower end or upper end of the allowed range. For BWP <bb>. \n
			:param cell_name: No help available
			:param starting_prb: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('starting_prb', starting_prb, DataType.Enum, enums.LowHigh))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUCCh:SPRB {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.LowHigh:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUCCh:SPRB \n
		Snippet: value: enums.LowHigh = driver.configure.signaling.nradio.cell.bwp.pucch.sprb.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the position of the resource blocks: lower end or upper end of the allowed range. For BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: starting_prb: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUCCh:SPRB? {param}')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
