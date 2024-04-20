from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K2Cls:
	"""K2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k2", core, parent)

	def set(self, cell_name: str, k_2: int or bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:CSSCheduling:K2 \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.csScheduling.k2.set(cell_name = 'abc', k_2 = 1) \n
		Sends a slot offset as 'minimumSchedulingOffsetK2-r16' to the UE, for the initial BWP. The slot offset defines the
		minimum allowed k2 value (offset between PDCCH and PUSCH, cross-slot scheduling) . \n
			:param cell_name: No help available
			:param k_2: (integer or boolean) integer: Send this value. OFF: Do not send a value.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('k_2', k_2, DataType.IntegerExt))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:CSSCheduling:K2 {param}'.rstrip())

	def get(self, cell_name: str) -> int or bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:CSSCheduling:K2 \n
		Snippet: value: int or bool = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.csScheduling.k2.get(cell_name = 'abc') \n
		Sends a slot offset as 'minimumSchedulingOffsetK2-r16' to the UE, for the initial BWP. The slot offset defines the
		minimum allowed k2 value (offset between PDCCH and PUSCH, cross-slot scheduling) . \n
			:param cell_name: No help available
			:return: k_2: (integer or boolean) integer: Send this value. OFF: Do not send a value."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:CSSCheduling:K2? {param}')
		return Conversions.str_to_int_or_bool(response)
