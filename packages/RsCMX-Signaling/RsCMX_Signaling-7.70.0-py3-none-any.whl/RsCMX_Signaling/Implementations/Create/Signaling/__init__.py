from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 19 total commands, 6 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def topology(self):
		"""topology commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Topology import TopologyCls
			self._topology = TopologyCls(self._core, self._cmd_group)
		return self._topology

	@property
	def etws(self):
		"""etws commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_etws'):
			from .Etws import EtwsCls
			self._etws = EtwsCls(self._core, self._cmd_group)
		return self._etws

	@property
	def ccopy(self):
		"""ccopy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccopy'):
			from .Ccopy import CcopyCls
			self._ccopy = CcopyCls(self._core, self._cmd_group)
		return self._ccopy

	@property
	def lte(self):
		"""lte commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	@property
	def awgn(self):
		"""awgn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	def set_cmas(self, network_scope: str) -> None:
		"""SCPI: CREate:SIGNaling:CMAS \n
		Snippet: driver.create.signaling.set_cmas(network_scope = 'abc') \n
		Creates a CMAS service for all cells in a certain <NetworkScope>. Use this network scope in the other CMAS commands. \n
			:param network_scope: Name of a PLMN or a tracking area or a cell
		"""
		param = Conversions.value_to_quoted_str(network_scope)
		self._core.io.write(f'CREate:SIGNaling:CMAS {param}')

	def set_rf_channel(self, cell_name: str) -> None:
		"""SCPI: CREate:SIGNaling:RFCHannel \n
		Snippet: driver.create.signaling.set_rf_channel(cell_name = 'abc') \n
		No command help available \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'CREate:SIGNaling:RFCHannel {param}')

	def set_fading(self, cell_name: str) -> None:
		"""SCPI: CREate:SIGNaling:FADing \n
		Snippet: driver.create.signaling.set_fading(cell_name = 'abc') \n
		Allows fading and reserves the required resources. Send this command before switching to live mode. \n
			:param cell_name: No help available
		"""
		param = Conversions.value_to_quoted_str(cell_name)
		self._core.io.write(f'CREate:SIGNaling:FADing {param}')

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
