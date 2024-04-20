from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BeamformingCls:
	"""Beamforming commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("beamforming", core, parent)

	def set(self, cell_name: str, beam_no_ports: enums.BeamNoPorts) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ANTenna:BEAMforming \n
		Snippet: driver.configure.signaling.lte.cell.antenna.beamforming.set(cell_name = 'abc', beam_no_ports = enums.BeamNoPorts.NONE) \n
		Sets the number of beamforming antenna ports. \n
			:param cell_name: No help available
			:param beam_no_ports: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('beam_no_ports', beam_no_ports, DataType.Enum, enums.BeamNoPorts))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:ANTenna:BEAMforming {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.BeamNoPorts:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ANTenna:BEAMforming \n
		Snippet: value: enums.BeamNoPorts = driver.configure.signaling.lte.cell.antenna.beamforming.get(cell_name = 'abc') \n
		Sets the number of beamforming antenna ports. \n
			:param cell_name: No help available
			:return: beam_no_ports: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:ANTenna:BEAMforming? {param}')
		return Conversions.str_to_scalar_enum(response, enums.BeamNoPorts)
