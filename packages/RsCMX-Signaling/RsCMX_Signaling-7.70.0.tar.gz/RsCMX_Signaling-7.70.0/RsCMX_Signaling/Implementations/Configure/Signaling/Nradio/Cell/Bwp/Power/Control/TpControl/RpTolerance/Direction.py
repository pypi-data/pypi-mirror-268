from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DirectionCls:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def set(self, cell_name: str, direction: enums.TpcDirection, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl:RPTolerance:DIRection \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.power.control.tpControl.rpTolerance.direction.set(cell_name = 'abc', direction = enums.TpcDirection.ALTernating, bwParts = repcap.BwParts.Default) \n
		Selects the direction of the TPC pattern for relative power tolerance tests, for BWP <bb>. \n
			:param cell_name: No help available
			:param direction: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('direction', direction, DataType.Enum, enums.TpcDirection))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl:RPTolerance:DIRection {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.TpcDirection:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl:RPTolerance:DIRection \n
		Snippet: value: enums.TpcDirection = driver.configure.signaling.nradio.cell.bwp.power.control.tpControl.rpTolerance.direction.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the direction of the TPC pattern for relative power tolerance tests, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: direction: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl:RPTolerance:DIRection? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TpcDirection)
