from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SprbCls:
	"""Sprb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sprb", core, parent)

	def set(self, cell_name: str, starting_prb: enums.LowHigh) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUCCh:SPRB \n
		Snippet: driver.configure.signaling.nradio.cell.pucch.sprb.set(cell_name = 'abc', starting_prb = enums.LowHigh.HIGH) \n
		Selects the position of the resource blocks: lower end or upper end of the allowed range. For the initial BWP. \n
			:param cell_name: No help available
			:param starting_prb: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('starting_prb', starting_prb, DataType.Enum, enums.LowHigh))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:PUCCh:SPRB {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.LowHigh:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:PUCCh:SPRB \n
		Snippet: value: enums.LowHigh = driver.configure.signaling.nradio.cell.pucch.sprb.get(cell_name = 'abc') \n
		Selects the position of the resource blocks: lower end or upper end of the allowed range. For the initial BWP. \n
			:param cell_name: No help available
			:return: starting_prb: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:PUCCh:SPRB? {param}')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
