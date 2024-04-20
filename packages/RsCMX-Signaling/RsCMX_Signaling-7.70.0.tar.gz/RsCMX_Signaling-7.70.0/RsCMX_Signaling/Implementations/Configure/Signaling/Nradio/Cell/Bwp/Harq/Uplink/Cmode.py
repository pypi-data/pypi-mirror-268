from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmodeCls:
	"""Cmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeC, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:CMODe \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.harq.uplink.cmode.set(cell_name = 'abc', mode = enums.ModeC.AUTO, bwParts = repcap.BwParts.Default) \n
		Selects a mode for UL HARQ configuration, for BWP <bb>. \n
			:param cell_name: No help available
			:param mode: NOTC: no UL HARQ AUTO: automatic configuration of the UL HARQ settings USER: user-defined configuration of the UL HARQ settings
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeC))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:CMODe {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.ModeC:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:UL:CMODe \n
		Snippet: value: enums.ModeC = driver.configure.signaling.nradio.cell.bwp.harq.uplink.cmode.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects a mode for UL HARQ configuration, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mode: NOTC: no UL HARQ AUTO: automatic configuration of the UL HARQ settings USER: user-defined configuration of the UL HARQ settings"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:UL:CMODe? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeC)
