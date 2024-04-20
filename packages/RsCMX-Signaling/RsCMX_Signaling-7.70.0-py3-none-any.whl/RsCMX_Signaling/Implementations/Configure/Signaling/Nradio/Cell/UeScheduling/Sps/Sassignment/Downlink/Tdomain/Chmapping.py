from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChmappingCls:
	"""Chmapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chmapping", core, parent)

	def set(self, cell_name: str, mapping: enums.Mapping) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:DL:TDOMain:CHMapping \n
		Snippet: driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.downlink.tdomain.chmapping.set(cell_name = 'abc', mapping = enums.Mapping.A) \n
		Selects the type of PDSCH mapping, for DL SPS scheduling, for the initial BWP. \n
			:param cell_name: No help available
			:param mapping: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mapping', mapping, DataType.Enum, enums.Mapping))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:DL:TDOMain:CHMapping {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Mapping:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:DL:TDOMain:CHMapping \n
		Snippet: value: enums.Mapping = driver.configure.signaling.nradio.cell.ueScheduling.sps.sassignment.downlink.tdomain.chmapping.get(cell_name = 'abc') \n
		Selects the type of PDSCH mapping, for DL SPS scheduling, for the initial BWP. \n
			:param cell_name: No help available
			:return: mapping: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:UESCheduling:SPS:SASSignment:DL:TDOMain:CHMapping? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Mapping)
