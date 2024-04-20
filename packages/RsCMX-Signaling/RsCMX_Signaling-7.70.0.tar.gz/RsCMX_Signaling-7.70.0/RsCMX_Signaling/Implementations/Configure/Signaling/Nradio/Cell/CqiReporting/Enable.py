from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, cell_name: str, enable: enums.EnableCqi) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:ENABle \n
		Snippet: driver.configure.signaling.nradio.cell.cqiReporting.enable.set(cell_name = 'abc', enable = enums.EnableCqi.APERiodic) \n
		Selects the CSI reporting type. \n
			:param cell_name: No help available
			:param enable: OFF: no reporting PERiodic: periodic CSI reporting APERiodic: aperiodic CSI reporting SPERsistant: semi-persistent CSI reporting
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('enable', enable, DataType.Enum, enums.EnableCqi))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.EnableCqi:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:ENABle \n
		Snippet: value: enums.EnableCqi = driver.configure.signaling.nradio.cell.cqiReporting.enable.get(cell_name = 'abc') \n
		Selects the CSI reporting type. \n
			:param cell_name: No help available
			:return: enable: OFF: no reporting PERiodic: periodic CSI reporting APERiodic: aperiodic CSI reporting SPERsistant: semi-persistent CSI reporting"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:ENABle? {param}')
		return Conversions.str_to_scalar_enum(response, enums.EnableCqi)
