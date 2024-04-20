from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsourceCls:
	"""Rsource commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsource", core, parent)

	def set(self, cell_name: str, ref_source: enums.SrcType) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:AUTO:RSOurce \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.auto.rsource.set(cell_name = 'abc', ref_source = enums.SrcType.PUCC) \n
		Sets the reference source for automatic configuration of expected UL power. \n
			:param cell_name: No help available
			:param ref_source: PUSC: PUSCH PUCC: PUCCH PUPU: PUCCH and PUSCH
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ref_source', ref_source, DataType.Enum, enums.SrcType))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:AUTO:RSOurce {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.SrcType:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:AUTO:RSOurce \n
		Snippet: value: enums.SrcType = driver.configure.signaling.lte.cell.power.uplink.auto.rsource.get(cell_name = 'abc') \n
		Sets the reference source for automatic configuration of expected UL power. \n
			:param cell_name: No help available
			:return: ref_source: PUSC: PUSCH PUCC: PUCCH PUPU: PUCCH and PUSCH"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:AUTO:RSOurce? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SrcType)
