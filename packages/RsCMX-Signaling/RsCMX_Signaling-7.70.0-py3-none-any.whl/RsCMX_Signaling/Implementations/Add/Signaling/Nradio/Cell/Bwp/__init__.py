from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwpCls:
	"""Bwp commands group definition. 5 total commands, 3 Subgroups, 1 group commands
	Repeated Capability: BwParts, default value after init: BwParts.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwp", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bwParts_get', 'repcap_bwParts_set', repcap.BwParts.Nr1)

	def repcap_bwParts_set(self, bwParts: repcap.BwParts) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BwParts.Default
		Default value after init: BwParts.Nr1"""
		self._cmd_group.set_repcap_enum_value(bwParts)

	def repcap_bwParts_get(self) -> repcap.BwParts:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def csi(self):
		"""csi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import CsiCls
			self._csi = CsiCls(self._core, self._cmd_group)
		return self._csi

	@property
	def harq(self):
		"""harq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import HarqCls
			self._harq = HarqCls(self._core, self._cmd_group)
		return self._harq

	@property
	def srs(self):
		"""srs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import SrsCls
			self._srs = SrsCls(self._core, self._cmd_group)
		return self._srs

	def set_value(self, cell_name: str) -> None:
		"""SCPI: ADD:SIGNaling:NRADio:CELL:BWP \n
		Snippet: driver.add.signaling.nradio.cell.bwp.set_value(cell_name = 'abc') \n
		Adds a bandwidth part (BWP) to the cell. The initial BWP is always available. Additional BWPs are numbered 1 to n. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'ADD:SIGNaling:NRADio:CELL:BWP {param}')

	def clone(self) -> 'BwpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
