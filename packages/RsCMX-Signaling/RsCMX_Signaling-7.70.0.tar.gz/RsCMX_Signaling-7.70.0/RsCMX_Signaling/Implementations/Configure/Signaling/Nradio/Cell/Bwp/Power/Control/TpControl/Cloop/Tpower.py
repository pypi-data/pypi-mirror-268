from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpowerCls:
	"""Tpower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpower", core, parent)

	def set(self, cell_name: str, power: float, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl:CLOop:TPOWer \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.power.control.tpControl.cloop.tpower.set(cell_name = 'abc', power = 1.0, bwParts = repcap.BwParts.Default) \n
		Defines the target power for closed-loop power control, for BWP <bb>. \n
			:param cell_name: No help available
			:param power: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('power', power, DataType.Float))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl:CLOop:TPOWer {param}'.rstrip())

	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> float:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl:CLOop:TPOWer \n
		Snippet: value: float = driver.configure.signaling.nradio.cell.bwp.power.control.tpControl.cloop.tpower.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Defines the target power for closed-loop power control, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: power: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl:CLOop:TPOWer? {param}')
		return Conversions.str_to_float(response)
