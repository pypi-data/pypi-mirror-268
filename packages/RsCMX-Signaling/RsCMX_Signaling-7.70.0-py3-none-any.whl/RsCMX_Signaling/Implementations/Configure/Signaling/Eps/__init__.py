from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 22 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	@property
	def nbehavior(self):
		"""nbehavior commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_nbehavior'):
			from .Nbehavior import NbehaviorCls
			self._nbehavior = NbehaviorCls(self._core, self._cmd_group)
		return self._nbehavior

	@property
	def dbearer(self):
		"""dbearer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dbearer'):
			from .Dbearer import DbearerCls
			self._dbearer = DbearerCls(self._core, self._cmd_group)
		return self._dbearer

	@property
	def nas(self):
		"""nas commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nas'):
			from .Nas import NasCls
			self._nas = NasCls(self._core, self._cmd_group)
		return self._nas

	@property
	def asPy(self):
		"""asPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_asPy'):
			from .AsPy import AsPyCls
			self._asPy = AsPyCls(self._core, self._cmd_group)
		return self._asPy

	@property
	def ueCapability(self):
		"""ueCapability commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_ueCapability'):
			from .UeCapability import UeCapabilityCls
			self._ueCapability = UeCapabilityCls(self._core, self._cmd_group)
		return self._ueCapability

	def get_tmode(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:EPS:TMODe \n
		Snippet: value: bool = driver.configure.signaling.eps.get_tmode() \n
		Selects whether an 'ACTIVATE TEST MODE' message is sent to the UE during registration in an EPS tracking area, or not.
		Configure this setting before registration. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:EPS:TMODe?')
		return Conversions.str_to_bool(response)

	def set_tmode(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:EPS:TMODe \n
		Snippet: driver.configure.signaling.eps.set_tmode(enable = False) \n
		Selects whether an 'ACTIVATE TEST MODE' message is sent to the UE during registration in an EPS tracking area, or not.
		Configure this setting before registration. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:EPS:TMODe {param}')

	def clone(self) -> 'EpsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EpsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
