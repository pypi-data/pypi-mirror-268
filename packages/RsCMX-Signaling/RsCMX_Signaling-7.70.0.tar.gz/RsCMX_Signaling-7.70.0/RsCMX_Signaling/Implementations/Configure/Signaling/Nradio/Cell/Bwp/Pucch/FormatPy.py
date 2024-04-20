from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, cell_name: str, format_py: enums.CellPucchFormatPy, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUCCh:FORMat \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.pucch.formatPy.set(cell_name = 'abc', format_py = enums.CellPucchFormatPy.F0, bwParts = repcap.BwParts.Default) \n
		Selects the PUCCH format for BWP <bb>. \n
			:param cell_name: No help available
			:param format_py: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('format_py', format_py, DataType.Enum, enums.CellPucchFormatPy))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUCCh:FORMat {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.CellPucchFormatPy:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:PUCCh:FORMat \n
		Snippet: value: enums.CellPucchFormatPy = driver.configure.signaling.nradio.cell.bwp.pucch.formatPy.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the PUCCH format for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: format_py: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:PUCCh:FORMat? {param}')
		return Conversions.str_to_scalar_enum(response, enums.CellPucchFormatPy)
