from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpControlCls:
	"""TpControl commands group definition. 6 total commands, 2 Subgroups, 1 group commands"""

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

	def set(self, cell_name: str, control: enums.Control) -> None:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl \n
		Snippet: driver.configure.signaling.lte.cell.power.control.tpControl.set(cell_name = 'abc', control = enums.Control.CLOop) \n
		Selects the pattern of TPC commands to be sent to the UE. \n
			:param cell_name: No help available
			:param control: Keep, min, max, closed loop, TPC pattern.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('control', control, DataType.Enum, enums.Control))
		self._core.io.write(f'CONFigure:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, cell_name: str) -> enums.Control:
		"""SCPI: [CONFigure]:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl \n
		Snippet: value: enums.Control = driver.configure.signaling.lte.cell.power.control.tpControl.get(cell_name = 'abc') \n
		Selects the pattern of TPC commands to be sent to the UE. \n
			:param cell_name: No help available
			:return: control: Keep, min, max, closed loop, TPC pattern."""
		param = Conversions.value_to_quoted_str(cell_name)
		response = self._core.io.query_str(f'CONFigure:SIGNaling:LTE:CELL:POWer:CONTrol:TPControl? {param}')
		return Conversions.str_to_scalar_enum(response, enums.Control)

	def clone(self) -> 'TpControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TpControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
