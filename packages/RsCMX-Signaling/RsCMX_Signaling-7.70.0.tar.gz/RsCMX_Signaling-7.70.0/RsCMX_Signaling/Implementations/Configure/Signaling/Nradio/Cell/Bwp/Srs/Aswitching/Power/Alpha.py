from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlphaCls:
	"""Alpha commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpha", core, parent)

	def set(self, cell_name: str, alpha: enums.Alpha, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:ASWitching:POWer:ALPHa \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.srs.aswitching.power.alpha.set(cell_name = 'abc', alpha = enums.Alpha.A00, bwParts = repcap.BwParts.Default) \n
		Sets the SRS power control parameter 'alpha' for SRS antenna switching, for BWP <bb>. \n
			:param cell_name: No help available
			:param alpha: Axy means x.y.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('alpha', alpha, DataType.Enum, enums.Alpha))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:ASWitching:POWer:ALPHa {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Alpha:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:SRS:ASWitching:POWer:ALPHa \n
		Snippet: value: enums.Alpha = driver.configure.signaling.nradio.cell.bwp.srs.aswitching.power.alpha.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Sets the SRS power control parameter 'alpha' for SRS antenna switching, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: alpha: Axy means x.y."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:SRS:ASWitching:POWer:ALPHa? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Alpha)
