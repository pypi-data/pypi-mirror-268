from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsirsPortsCls:
	"""CsirsPorts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csirsPorts", core, parent)

	def set(self, cell_name: str, ant_no_ports: enums.Ports) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:CSIRsports \n
		Snippet: driver.configure.signaling.nradio.cell.mconfig.csirsPorts.set(cell_name = 'abc', ant_no_ports = enums.Ports.P1) \n
		Selects the maximum number of CSI-RS antenna ports allowed in live mode. \n
			:param cell_name: No help available
			:param ant_no_ports: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ant_no_ports', ant_no_ports, DataType.Enum, enums.Ports))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:CSIRsports {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Ports:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:MCONfig:CSIRsports \n
		Snippet: value: enums.Ports = driver.configure.signaling.nradio.cell.mconfig.csirsPorts.get(cell_name = 'abc') \n
		Selects the maximum number of CSI-RS antenna ports allowed in live mode. \n
			:param cell_name: No help available
			:return: ant_no_ports: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:MCONfig:CSIRsports? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Ports)
