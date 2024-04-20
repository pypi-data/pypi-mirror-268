from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 26 total commands, 6 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def topology(self):
		"""topology commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_topology'):
			from .Topology import TopologyCls
			self._topology = TopologyCls(self._core, self._cmd_group)
		return self._topology

	@property
	def eps(self):
		"""eps commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eps'):
			from .Eps import EpsCls
			self._eps = EpsCls(self._core, self._cmd_group)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fgs'):
			from .Fgs import FgsCls
			self._fgs = FgsCls(self._core, self._cmd_group)
		return self._fgs

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import TriggerCls
			self._trigger = TriggerCls(self._core, self._cmd_group)
		return self._trigger

	@property
	def lte(self):
		"""lte commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def nradio(self):
		"""nradio commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	def get_ue(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:UE \n
		Snippet: value: List[str] = driver.catalog.signaling.get_ue() \n
		No command help available \n
			:return: ue_name: No help available
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:UE?')
		return Conversions.str_to_str_list(response)

	def get_rf_channel(self) -> List[str]:
		"""SCPI: CATalog:SIGNaling:RFCHannel \n
		Snippet: value: List[str] = driver.catalog.signaling.get_rf_channel() \n
		No command help available \n
			:return: cell_name: No help available
		"""
		response = self._core.io.query_str('CATalog:SIGNaling:RFCHannel?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
