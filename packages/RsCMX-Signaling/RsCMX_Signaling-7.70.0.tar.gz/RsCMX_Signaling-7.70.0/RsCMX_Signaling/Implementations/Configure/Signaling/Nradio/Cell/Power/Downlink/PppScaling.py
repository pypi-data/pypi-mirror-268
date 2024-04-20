from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PppScalingCls:
	"""PppScaling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pppScaling", core, parent)

	def set(self, cell_name: str, power_scaling: enums.PowerScaling) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:PPPScaling \n
		Snippet: driver.configure.signaling.nradio.cell.power.downlink.pppScaling.set(cell_name = 'abc', power_scaling = enums.PowerScaling.TGPP) \n
		Defines the PDSCH power scaling depending on the number of layers. \n
			:param cell_name: No help available
			:param power_scaling:
				- TGPP: 3GPP compliant - the power per layer decreases with increasing number of layers, so that the total power of the PDSCH over all layers is the same as for single-layer transmission.
				- TOPTimized: Throughput optimized - the total power of the PDSCH increases with increasing number of layers (double number of layers means plus 3 dB) ."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('power_scaling', power_scaling, DataType.Enum, enums.PowerScaling))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:PPPScaling {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PowerScaling:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:POWer:DL:PPPScaling \n
		Snippet: value: enums.PowerScaling = driver.configure.signaling.nradio.cell.power.downlink.pppScaling.get(cell_name = 'abc') \n
		Defines the PDSCH power scaling depending on the number of layers. \n
			:param cell_name: No help available
			:return: power_scaling:
				- TGPP: 3GPP compliant - the power per layer decreases with increasing number of layers, so that the total power of the PDSCH over all layers is the same as for single-layer transmission.
				- TOPTimized: Throughput optimized - the total power of the PDSCH increases with increasing number of layers (double number of layers means plus 3 dB) ."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:POWer:DL:PPPScaling? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PowerScaling)
