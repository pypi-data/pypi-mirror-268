from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IraCls:
	"""Ira commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ira", core, parent)

	def set(self, cell_name: str, ira: enums.Ira) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:IRA \n
		Snippet: driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.ira.set(cell_name = 'abc', ira = enums.Ira.E2) \n
		Configures the number of empty transmissions before implicit release of the UL grant, for SPS scheduling. \n
			:param cell_name: No help available
			:param ira: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ira', ira, DataType.Enum, enums.Ira))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:IRA {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Ira:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:IRA \n
		Snippet: value: enums.Ira = driver.configure.signaling.lte.cell.ueScheduling.sps.sassignment.uplink.ira.get(cell_name = 'abc') \n
		Configures the number of empty transmissions before implicit release of the UL grant, for SPS scheduling. \n
			:param cell_name: No help available
			:return: ira: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:UESCheduling:SPS:SASSignment:UL:IRA? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Ira)
