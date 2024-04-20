from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TrsCls:
	"""Trs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trs", core, parent)

	def delete(self, cell_name: str, index: int) -> None:
		"""SCPI: DELete:SIGNaling:NRADio:CELL:CSI:TRS \n
		Snippet: driver.signaling.nradio.cell.csi.trs.delete(cell_name = 'abc', index = 1) \n
		Deletes the TRS <Index>, for the initial BWP. \n
			:param cell_name: No help available
			:param index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		self._core.io.write(f'DELete:SIGNaling:NRADio:CELL:CSI:TRS {param}'.rstrip())
