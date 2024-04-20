from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SignalingCls:
	"""Signaling commands group definition. 899 total commands, 16 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signaling", core, parent)

	@property
	def topology(self):
		"""topology commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_topology'):
			from .Topology import TopologyCls
			self._topology = TopologyCls(self._core, self._cmd_group)
		return self._topology

	@property
	def nbehavior(self):
		"""nbehavior commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbehavior'):
			from .Nbehavior import NbehaviorCls
			self._nbehavior = NbehaviorCls(self._core, self._cmd_group)
		return self._nbehavior

	@property
	def eps(self):
		"""eps commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_eps'):
			from .Eps import EpsCls
			self._eps = EpsCls(self._core, self._cmd_group)
		return self._eps

	@property
	def fgs(self):
		"""fgs commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_fgs'):
			from .Fgs import FgsCls
			self._fgs = FgsCls(self._core, self._cmd_group)
		return self._fgs

	@property
	def ue(self):
		"""ue commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ue'):
			from .Ue import UeCls
			self._ue = UeCls(self._core, self._cmd_group)
		return self._ue

	@property
	def sms(self):
		"""sms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sms'):
			from .Sms import SmsCls
			self._sms = SmsCls(self._core, self._cmd_group)
		return self._sms

	@property
	def tmode(self):
		"""tmode commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_tmode'):
			from .Tmode import TmodeCls
			self._tmode = TmodeCls(self._core, self._cmd_group)
		return self._tmode

	@property
	def cmas(self):
		"""cmas commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmas'):
			from .Cmas import CmasCls
			self._cmas = CmasCls(self._core, self._cmd_group)
		return self._cmas

	@property
	def etws(self):
		"""etws commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_etws'):
			from .Etws import EtwsCls
			self._etws = EtwsCls(self._core, self._cmd_group)
		return self._etws

	@property
	def ueAssistance(self):
		"""ueAssistance commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ueAssistance'):
			from .UeAssistance import UeAssistanceCls
			self._ueAssistance = UeAssistanceCls(self._core, self._cmd_group)
		return self._ueAssistance

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import TriggerCls
			self._trigger = TriggerCls(self._core, self._cmd_group)
		return self._trigger

	@property
	def lte(self):
		"""lte commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import LteCls
			self._lte = LteCls(self._core, self._cmd_group)
		return self._lte

	@property
	def measurement(self):
		"""measurement commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import MeasurementCls
			self._measurement = MeasurementCls(self._core, self._cmd_group)
		return self._measurement

	@property
	def nradio(self):
		"""nradio commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nradio'):
			from .Nradio import NradioCls
			self._nradio = NradioCls(self._core, self._cmd_group)
		return self._nradio

	@property
	def fading(self):
		"""fading commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Fading import FadingCls
			self._fading = FadingCls(self._core, self._cmd_group)
		return self._fading

	@property
	def awgn(self):
		"""awgn commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import AwgnCls
			self._awgn = AwgnCls(self._core, self._cmd_group)
		return self._awgn

	def get_mc_group(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:MCGRoup \n
		Snippet: value: str = driver.configure.signaling.get_mc_group() \n
		No command help available \n
			:return: cell_group_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MCGRoup?')
		return trim_str_response(response)

	def get_sc_group(self) -> str:
		"""SCPI: [CONFigure]:SIGNaling:SCGRoup \n
		Snippet: value: str = driver.configure.signaling.get_sc_group() \n
		No command help available \n
			:return: cell_group_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:SCGRoup?')
		return trim_str_response(response)

	def get_ap_mod(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:APMod \n
		Snippet: value: bool = driver.configure.signaling.get_ap_mod() \n
		Selects whether changes are applied automatically. Applying several commands simultaneously can be necessary to avoid
		call drops caused by intermediate combinations of settings. \n
			:return: enable:
				- ON: If you modify settings via a command, the changes are applied immediately (known default behavior) .
				- OFF: Changes are not applied automatically. Use the command PROCedure:SIGNaling:APMod to apply pending changes.This behavior corresponds to a dialog box with an apply button, where you apply several changes simultaneously."""
		response = self._core.io.query_str('CONFigure:SIGNaling:APMod?')
		return Conversions.str_to_bool(response)

	def set_ap_mod(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:APMod \n
		Snippet: driver.configure.signaling.set_ap_mod(enable = False) \n
		Selects whether changes are applied automatically. Applying several commands simultaneously can be necessary to avoid
		call drops caused by intermediate combinations of settings. \n
			:param enable:
				- ON: If you modify settings via a command, the changes are applied immediately (known default behavior) .
				- OFF: Changes are not applied automatically. Use the command PROCedure:SIGNaling:APMod to apply pending changes.This behavior corresponds to a dialog box with an apply button, where you apply several changes simultaneously."""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:APMod {param}')

	def clone(self) -> 'SignalingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SignalingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
