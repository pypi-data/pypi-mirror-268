from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FgsCls:
	"""Fgs commands group definition. 27 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fgs", core, parent)

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
		"""ueCapability commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_ueCapability'):
			from .UeCapability import UeCapabilityCls
			self._ueCapability = UeCapabilityCls(self._core, self._cmd_group)
		return self._ueCapability

	@property
	def cnPaging(self):
		"""cnPaging commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cnPaging'):
			from .CnPaging import CnPagingCls
			self._cnPaging = CnPagingCls(self._core, self._cmd_group)
		return self._cnPaging

	def get_tmode(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:TMODe \n
		Snippet: value: bool = driver.configure.signaling.fgs.get_tmode() \n
		Selects whether an 'ACTIVATE TEST MODE' message is sent to the UE during registration in a 5GS tracking area, or not.
		Configure this setting before registration. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:TMODe?')
		return Conversions.str_to_bool(response)

	def set_tmode(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:TMODe \n
		Snippet: driver.configure.signaling.fgs.set_tmode(enable = False) \n
		Selects whether an 'ACTIVATE TEST MODE' message is sent to the UE during registration in a 5GS tracking area, or not.
		Configure this setting before registration. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:TMODe {param}')

	def clone(self) -> 'FgsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FgsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
