from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoVsssCls:
	"""PoVsss commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poVsss", core, parent)

	def set(self, cell_name: str, power: enums.RsrcPower) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:RESource:POVSss \n
		Snippet: driver.configure.signaling.nradio.cell.cqiReporting.resource.poVsss.set(cell_name = 'abc', power = enums.RsrcPower.M3DB) \n
		Configures the power offset of NZP CSI-RS RE to SSS RE. \n
			:param cell_name: No help available
			:param power: -9 dB, -6 dB, -3 dB, 0 dB, +3 dB, +6 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('power', power, DataType.Enum, enums.RsrcPower))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:RESource:POVSss {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.RsrcPower:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:CQIReporting:RESource:POVSss \n
		Snippet: value: enums.RsrcPower = driver.configure.signaling.nradio.cell.cqiReporting.resource.poVsss.get(cell_name = 'abc') \n
		Configures the power offset of NZP CSI-RS RE to SSS RE. \n
			:param cell_name: No help available
			:return: power: -9 dB, -6 dB, -3 dB, 0 dB, +3 dB, +6 dB"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:CQIReporting:RESource:POVSss? {param}')
		return Conversions.str_to_scalar_enum(response, enums.RsrcPower)
