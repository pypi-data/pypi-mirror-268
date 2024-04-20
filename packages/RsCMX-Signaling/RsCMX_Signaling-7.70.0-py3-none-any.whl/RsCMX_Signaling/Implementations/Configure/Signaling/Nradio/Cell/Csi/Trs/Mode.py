from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, cell_name: str, mode: enums.ModeTrs) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CSI:TRS:MODE \n
		Snippet: driver.configure.signaling.nradio.cell.csi.trs.mode.set(cell_name = 'abc', mode = enums.ModeTrs.DEF) \n
		Selects the configuration mode for TRS transmission, for the initial BWP. \n
			:param cell_name: No help available
			:param mode: OFF: no TRS DEF: TRS according to 3GPP TS 38.508 UDEF: user-defined TRS
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mode', mode, DataType.Enum, enums.ModeTrs))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CSI:TRS:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.ModeTrs:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CSI:TRS:MODE \n
		Snippet: value: enums.ModeTrs = driver.configure.signaling.nradio.cell.csi.trs.mode.get(cell_name = 'abc') \n
		Selects the configuration mode for TRS transmission, for the initial BWP. \n
			:param cell_name: No help available
			:return: mode: OFF: no TRS DEF: TRS according to 3GPP TS 38.508 UDEF: user-defined TRS"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CSI:TRS:MODE? {param}')
		return Conversions.str_to_scalar_enum(response, enums.ModeTrs)
