from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrStepCls:
	"""PrStep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prStep", core, parent)

	def set(self, cell_name: str, pwr_ramping_step: enums.PwrRampingStepA) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:PRSTep \n
		Snippet: driver.configure.signaling.lte.cell.power.uplink.prStep.set(cell_name = 'abc', pwr_ramping_step = enums.PwrRampingStepA.S0) \n
		Defines the transmit power difference between two consecutive preambles (power ramping) . \n
			:param cell_name: No help available
			:param pwr_ramping_step: Step size in dB (0 dB to 6 dB)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('pwr_ramping_step', pwr_ramping_step, DataType.Enum, enums.PwrRampingStepA))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:PRSTep {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.PwrRampingStepA:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:UL:PRSTep \n
		Snippet: value: enums.PwrRampingStepA = driver.configure.signaling.lte.cell.power.uplink.prStep.get(cell_name = 'abc') \n
		Defines the transmit power difference between two consecutive preambles (power ramping) . \n
			:param cell_name: No help available
			:return: pwr_ramping_step: Step size in dB (0 dB to 6 dB)"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:UL:PRSTep? {param}')
		return Conversions.str_to_scalar_enum(response, enums.PwrRampingStepA)
