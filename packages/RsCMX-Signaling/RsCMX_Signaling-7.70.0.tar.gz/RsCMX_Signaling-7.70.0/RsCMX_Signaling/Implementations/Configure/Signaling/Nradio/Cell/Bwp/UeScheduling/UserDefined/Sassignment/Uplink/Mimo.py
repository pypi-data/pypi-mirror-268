from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	def set(self, cell_name: str, slot: int, mimo: enums.MimoB, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:UDEFined:SASSignment:UL:MIMO \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.sassignment.uplink.mimo.set(cell_name = 'abc', slot = 1, mimo = enums.MimoB.M22, bwParts = repcap.BwParts.Default) \n
		Specifies the MIMO scheme for the UL slot with the index <Slot>, for BWP <bb>. \n
			:param cell_name: No help available
			:param slot: No help available
			:param mimo: SISO: nx1 M22: nx2
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer), ArgSingle('mimo', mimo, DataType.Enum, enums.MimoB))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:UDEFined:SASSignment:UL:MIMO {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, slot: int, bwParts=repcap.BwParts.Default) -> enums.MimoB:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:UDEFined:SASSignment:UL:MIMO \n
		Snippet: value: enums.MimoB = driver.configure.signaling.nradio.cell.bwp.ueScheduling.userDefined.sassignment.uplink.mimo.get(cell_name = 'abc', slot = 1, bwParts = repcap.BwParts.Default) \n
		Specifies the MIMO scheme for the UL slot with the index <Slot>, for BWP <bb>. \n
			:param cell_name: No help available
			:param slot: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mimo: SISO: nx1 M22: nx2"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('slot', slot, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:UDEFined:SASSignment:UL:MIMO? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.MimoB)
