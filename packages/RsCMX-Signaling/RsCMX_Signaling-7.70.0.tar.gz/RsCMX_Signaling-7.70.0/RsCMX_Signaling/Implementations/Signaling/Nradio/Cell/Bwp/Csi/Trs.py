from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrsCls:
	"""Trs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trs", core, parent)

	def delete(self, cell_name: str, index: int, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL:BWP<bwp_id>:CSI:TRS \n
		Snippet: driver.signaling.nradio.cell.bwp.csi.trs.delete(cell_name = 'abc', index = 1, bwParts = repcap.BwParts.Default) \n
		Deletes the TRS <Index>, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:CSI:TRS {param}'.rstrip())
