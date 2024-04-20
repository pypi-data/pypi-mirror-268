from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.Types import DataType
from ............Internal.ArgSingleList import ArgSingleList
from ............Internal.ArgSingle import ArgSingle
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChmappingCls:
	"""Chmapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chmapping", core, parent)

	def set(self, cell_name: str, mapping: enums.Mapping, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:SASSignment:UL:TDOMain:CHMapping \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.sassignment.uplink.tdomain.chmapping.set(cell_name = 'abc', mapping = enums.Mapping.A, bwParts = repcap.BwParts.Default) \n
		Selects the type of PUSCH mapping, for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param mapping: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('mapping', mapping, DataType.Enum, enums.Mapping))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:SASSignment:UL:TDOMain:CHMapping {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.Mapping:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:UESCheduling:SPS:SASSignment:UL:TDOMain:CHMapping \n
		Snippet: value: enums.Mapping = driver.configure.signaling.nradio.cell.bwp.ueScheduling.sps.sassignment.uplink.tdomain.chmapping.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the type of PUSCH mapping, for UL configured grant, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: mapping: No help available"""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:UESCheduling:SPS:SASSignment:UL:TDOMain:CHMapping? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Mapping)
