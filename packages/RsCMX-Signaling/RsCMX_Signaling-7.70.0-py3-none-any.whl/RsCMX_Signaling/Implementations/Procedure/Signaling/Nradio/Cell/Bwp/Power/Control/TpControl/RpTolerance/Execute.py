from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExecuteCls:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self, cell_name: str, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: PROCedure:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl:RPTolerance:EXECute \n
		Snippet: driver.procedure.signaling.nradio.cell.bwp.power.control.tpControl.rpTolerance.execute.set(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Starts the execution of the TPC pattern for relative power tolerance tests, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'PROCedure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl:RPTolerance:EXECute {param}')
