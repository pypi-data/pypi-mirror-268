from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PortsCls:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def set(self, cell_name: str, ports: enums.Ports) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:RESource:PORTs \n
		Snippet: driver.configure.signaling.nradio.cell.cqiReporting.resource.ports.set(cell_name = 'abc', ports = enums.Ports.P1) \n
		Selects the number of CSI-RS ports, signaled as 'nrofPorts' in IE 'CSI-RS-ResourceMapping'. \n
			:param cell_name: No help available
			:param ports: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ports', ports, DataType.Enum, enums.Ports))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:RESource:PORTs {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Ports:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:RESource:PORTs \n
		Snippet: value: enums.Ports = driver.configure.signaling.nradio.cell.cqiReporting.resource.ports.get(cell_name = 'abc') \n
		Selects the number of CSI-RS ports, signaled as 'nrofPorts' in IE 'CSI-RS-ResourceMapping'. \n
			:param cell_name: No help available
			:return: ports: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:RESource:PORTs? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Ports)
