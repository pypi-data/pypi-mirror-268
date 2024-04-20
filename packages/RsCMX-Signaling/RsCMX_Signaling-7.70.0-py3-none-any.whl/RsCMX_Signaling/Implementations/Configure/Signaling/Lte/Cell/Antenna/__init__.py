from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AntennaCls:
	"""Antenna commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	@property
	def crSports(self):
		"""crSports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crSports'):
			from .CrSports import CrSportsCls
			self._crSports = CrSportsCls(self._core, self._cmd_group)
		return self._crSports

	@property
	def beamforming(self):
		"""beamforming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_beamforming'):
			from .Beamforming import BeamformingCls
			self._beamforming = BeamformingCls(self._core, self._cmd_group)
		return self._beamforming

	@property
	def streams(self):
		"""streams commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_streams'):
			from .Streams import StreamsCls
			self._streams = StreamsCls(self._core, self._cmd_group)
		return self._streams

	def set(self, cell_name: str, ant_no_ports: enums.AntNoPorts, beam_no_ports: enums.BeamNoPorts = None, dl_iq_data_streams: enums.DlIqDataStreams = None) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ANTenna \n
		Snippet: driver.configure.signaling.lte.cell.antenna.set(cell_name = 'abc', ant_no_ports = enums.AntNoPorts.P1, beam_no_ports = enums.BeamNoPorts.NONE, dl_iq_data_streams = enums.DlIqDataStreams.S1) \n
		Selects the number of antenna ports and streams. \n
			:param cell_name: No help available
			:param ant_no_ports: Number of CRS antenna ports.
			:param beam_no_ports: Beamforming number of antenna ports.
			:param dl_iq_data_streams: Number of I/Q data DL streams.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('ant_no_ports', ant_no_ports, DataType.Enum, enums.AntNoPorts), ArgSingle('beam_no_ports', beam_no_ports, DataType.Enum, enums.BeamNoPorts, is_optional=True), ArgSingle('dl_iq_data_streams', dl_iq_data_streams, DataType.Enum, enums.DlIqDataStreams, is_optional=True))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:ANTenna {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ant_No_Ports: enums.AntNoPorts: Number of CRS antenna ports.
			- Beam_No_Ports: enums.BeamNoPorts: Beamforming number of antenna ports.
			- Dl_Iq_Data_Streams: enums.DlIqDataStreams: Number of I/Q data DL streams."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Ant_No_Ports', enums.AntNoPorts),
			ArgStruct.scalar_enum('Beam_No_Ports', enums.BeamNoPorts),
			ArgStruct.scalar_enum('Dl_Iq_Data_Streams', enums.DlIqDataStreams)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ant_No_Ports: enums.AntNoPorts = None
			self.Beam_No_Ports: enums.BeamNoPorts = None
			self.Dl_Iq_Data_Streams: enums.DlIqDataStreams = None

	def get(self, cell_name: str) -> GetStruct:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:ANTenna \n
		Snippet: value: GetStruct = driver.configure.signaling.lte.cell.antenna.get(cell_name = 'abc') \n
		Selects the number of antenna ports and streams. \n
			:param cell_name: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(cell_name)
		return self._core.io.query_struct(f'CONFigure:SIGNaling:LTE:CELL:ANTenna? {param}', self.__class__.GetStruct())

	def clone(self) -> 'AntennaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AntennaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
