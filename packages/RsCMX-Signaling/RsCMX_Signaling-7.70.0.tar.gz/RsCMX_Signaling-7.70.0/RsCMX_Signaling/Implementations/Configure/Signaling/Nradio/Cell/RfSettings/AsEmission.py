from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AsEmissionCls:
	"""AsEmission commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asEmission", core, parent)

	def set(self, cell_name: str, as_emission: int or bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:ASEMission \n
		Snippet: driver.configure.signaling.nradio.cell.rfSettings.asEmission.set(cell_name = 'abc', as_emission = 1) \n
		Sets the parameter 'AdditionalSpectrumEmission', signaled to the UE if the value is not OFF. \n
			:param cell_name: No help available
			:param as_emission: (integer or boolean) No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('as_emission', as_emission, DataType.IntegerExt))
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:ASEMission {param}'.rstrip())

	def get(self, cell_name: str) -> int or bool:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:RFSettings:ASEMission \n
		Snippet: value: int or bool = driver.configure.signaling.nradio.cell.rfSettings.asEmission.get(cell_name = 'abc') \n
		Sets the parameter 'AdditionalSpectrumEmission', signaled to the UE if the value is not OFF. \n
			:param cell_name: No help available
			:return: as_emission: (integer or boolean) No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:RFSettings:ASEMission? {param}')
		return Conversions.str_to_int_or_bool(response)
