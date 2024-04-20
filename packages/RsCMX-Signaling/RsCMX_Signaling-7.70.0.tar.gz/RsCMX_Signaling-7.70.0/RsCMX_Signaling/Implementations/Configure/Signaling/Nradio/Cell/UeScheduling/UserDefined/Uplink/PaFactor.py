from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaFactorCls:
	"""PaFactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("paFactor", core, parent)

	def set(self, cell_name: str, factor: enums.UeScFactor) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PAFactor \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.paFactor.set(cell_name = 'abc', factor = enums.UeScFactor.N2) \n
		Defines the 'pusch-AggregationFactor' of the PUSCH configuration, signaled to the UE, for the initial BWP. \n
			:param cell_name: No help available
			:param factor: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('factor', factor, DataType.Enum, enums.UeScFactor))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PAFactor {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.UeScFactor:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PAFactor \n
		Snippet: value: enums.UeScFactor = driver.configure.signaling.nradio.cell.ueScheduling.userDefined.uplink.paFactor.get(cell_name = 'abc') \n
		Defines the 'pusch-AggregationFactor' of the PUSCH configuration, signaled to the UE, for the initial BWP. \n
			:param cell_name: No help available
			:return: factor: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:UDEFined:UL:PAFactor? {param}')
		return Conversions.str_to_scalar_enum(response, enums.UeScFactor)
