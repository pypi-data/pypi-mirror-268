from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbgSizeCls:
	"""RbgSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbgSize", core, parent)

	def set(self, cell_name: str, rgb_size: enums.RgbSize, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:UL:RBGSize \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.uplink.rbgSize.set(cell_name = 'abc', rgb_size = enums.RgbSize.CON1, bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'rbg-Size' for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param rgb_size: Config 1 or 2
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('rgb_size', rgb_size, DataType.Enum, enums.RgbSize))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:UL:RBGSize {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.RgbSize:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:UL:RBGSize \n
		Snippet: value: enums.RgbSize = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.uplink.rbgSize.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the signaled 'rbg-Size' for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: rgb_size: Config 1 or 2"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:UL:RBGSize? {param}')
		return Conversions.str_to_scalar_enum(response, enums.RgbSize)
