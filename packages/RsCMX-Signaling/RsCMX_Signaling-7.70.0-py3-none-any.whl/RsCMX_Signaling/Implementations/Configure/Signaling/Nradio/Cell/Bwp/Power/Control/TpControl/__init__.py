from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpControlCls:
	"""TpControl commands group definition. 9 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpControl", core, parent)

	@property
	def cloop(self):
		"""cloop commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cloop'):
			from .Cloop import CloopCls
			self._cloop = CloopCls(self._core, self._cmd_group)
		return self._cloop

	@property
	def pattern(self):
		"""pattern commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import PatternCls
			self._pattern = PatternCls(self._core, self._cmd_group)
		return self._pattern

	@property
	def rpTolerance(self):
		"""rpTolerance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rpTolerance'):
			from .RpTolerance import RpToleranceCls
			self._rpTolerance = RpToleranceCls(self._core, self._cmd_group)
		return self._rpTolerance

	def set(self, cell_name: str, control: enums.TpControl, bwParts=repcap.BwParts.Default) -> None:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl \n
		Snippet: driver.configure.signaling.nradio.cell.bwp.power.control.tpControl.set(cell_name = 'abc', control = enums.TpControl.CLOop, bwParts = repcap.BwParts.Default) \n
		Selects the pattern of TPC commands to be sent to the UE, for BWP <bb>. \n
			:param cell_name: No help available
			:param control: Keep, min, max, closed loop, TPC pattern, relative power tolerance.
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('control', control, DataType.Enum, enums.TpControl))
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		self._core.io.write(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str, bwParts=repcap.BwParts.Default) -> enums.TpControl:
		"""SCPI: [CONFigure]:SIGNaling:NRADio:CELL:BWP<bpwid>:POWer:CONTrol:TPControl \n
		Snippet: value: enums.TpControl = driver.configure.signaling.nradio.cell.bwp.power.control.tpControl.get(cell_name = 'abc', bwParts = repcap.BwParts.Default) \n
		Selects the pattern of TPC commands to be sent to the UE, for BWP <bb>. \n
			:param cell_name: No help available
			:param bwParts: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bwp')
			:return: control: Keep, min, max, closed loop, TPC pattern, relative power tolerance."""
		param = Conversions.value_to_quoted_str(cell_name)
		bwParts_cmd_val = self._cmd_group.get_repcap_cmd_value(bwParts, repcap.BwParts)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:NRADio:CELL:BWP{bwParts_cmd_val}:POWer:CONTrol:TPControl? {param}')
		return Conversions.str_to_scalar_enum(response, enums.TpControl)

	def clone(self) -> 'TpControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TpControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
