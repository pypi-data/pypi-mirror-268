from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, cell_name: str, index: int, modulation: enums.ModulationRetr, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:DL:USER:RETRansm:MODulation \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.harq.downlink.user.retransm.modulation.set(cell_name = 'abc', index = 1, modulation = enums.ModulationRetr.AUTO, bwParts = repcap.BwParts.Default) \n
		Selects a modulation scheme for a certain retransmission, for user-defined DL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param modulation: BPSK, auto mode, π/2-BPSK, QPSK, 16QAM, 64QAM, 256QAM, 1024QAM
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.ModulationRetr))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:DL:USER:RETRansm:MODulation {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, index: int, bwParts=repcap.BwParts.Default) -> enums.ModulationRetr:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bwp_id>:HARQ:DL:USER:RETRansm:MODulation \n
		Snippet: value: enums.ModulationRetr = driver.configure.signaling.nradio.cell.bwp.harq.downlink.user.retransm.modulation.get(cell_name = 'abc', index = 1, bwParts = repcap.BwParts.Default) \n
		Selects a modulation scheme for a certain retransmission, for user-defined DL HARQ, for BWP <bb>. \n
			:param cell_name: No help available
			:param index: Index of the retransmission
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: modulation: BPSK, auto mode, π/2-BPSK, QPSK, 16QAM, 64QAM, 256QAM, 1024QAM"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('index', index, DataType.Integer))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:HARQ:DL:USER:RETRansm:MODulation? {param}'.rstrip())
		return Conversions.str_to_scalar_enum(response, enums.ModulationRetr)
