from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodicityCls:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, cell_name: str, periodicity: enums.TadvPeriodicity, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:TADVance:PERiodicity \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.tadvance.periodicity.set(cell_name = 'abc', periodicity = enums.TadvPeriodicity.CONTinuous, bwParts = repcap.BwParts.Default) \n
		Configures the periodicity for sending timing advance commands to the UE, for BWP <bb>. \n
			:param cell_name: No help available
			:param periodicity: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('periodicity', periodicity, DataType.Enum, enums.TadvPeriodicity))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:TADVance:PERiodicity {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.TadvPeriodicity:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:TADVance:PERiodicity \n
		Snippet: value: enums.TadvPeriodicity = driver.configure.signaling.nradio.cell.bwp.tadvance.periodicity.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Configures the periodicity for sending timing advance commands to the UE, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: periodicity: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:TADVance:PERiodicity? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TadvPeriodicity)
