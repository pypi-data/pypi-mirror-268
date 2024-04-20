from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlIndicationCls:
	"""UlIndication commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulIndication", core, parent)

	def set(self, cell_name: str, indication: enums.UlIndication) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ULINdication \n
		Snippet: driver.configure.signaling.lte.cell.ulIndication.set(cell_name = 'abc', indication = enums.UlIndication.AOFF) \n
		Configures whether the optional parameter 'upperLayerIndication' is signaled to the UE in SIB 2 or not. \n
			:param cell_name: No help available
			:param indication: AUTO: Signaled if EN-DC is active for the LTE cell. AON: Always signaled. AOFF: Never signaled.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('indication', indication, DataType.Enum, enums.UlIndication))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:ULINdication {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.UlIndication:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ULINdication \n
		Snippet: value: enums.UlIndication = driver.configure.signaling.lte.cell.ulIndication.get(cell_name = 'abc') \n
		Configures whether the optional parameter 'upperLayerIndication' is signaled to the UE in SIB 2 or not. \n
			:param cell_name: No help available
			:return: indication: AUTO: Signaled if EN-DC is active for the LTE cell. AON: Always signaled. AOFF: Never signaled."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:ULINdication? {param}')
		return Conversions.str_to_scalar_enum(response, enums.UlIndication)
