from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeRvs) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RVSequence:MODE \n
		Snippet: driver.configure.signaling.lte.cell.harq.downlink.rvSequence.mode.set(cell_name = 'abc', mode = enums.ModeRvs.AUTO) \n
		Selects a mode for configuration of RV sequences. \n
			:param cell_name: No help available
			:param mode: Auto, 3GPP 36.101, user-defined
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeRvs))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RVSequence:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeRvs:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:HARQ:DL:RVSequence:MODE \n
		Snippet: value: enums.ModeRvs = driver.configure.signaling.lte.cell.harq.downlink.rvSequence.mode.get(cell_name = 'abc') \n
		Selects a mode for configuration of RV sequences. \n
			:param cell_name: No help available
			:return: mode: Auto, 3GPP 36.101, user-defined"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:HARQ:DL:RVSequence:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeRvs)
